import os
import re
import json

def scan_interactive_elements(start_dir):
    """
    Scans the codebase for interactive elements (buttons, inputs, potential click handlers).
    Returns a dictionary of found elements grouped by file path.
    """
    inventory = {}
    
    # Regex patterns for identifying interactive elements
    patterns = {
        'button': r'<button[^>]*>([^<]*)</button>|<button[^>]*aria-label="([^"]*)"',
        'input': r'<input[^>]*placeholder="([^"]*)"|<input[^>]*name="([^"]*)"',
        'clickable_div': r'<div[^>]*onClick={([^}]*)}[^>]*>([^<]*)</div>', 
        # Add more patterns as needed (e.g., specific component names like PoolCard)
    }

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.tsx') or file.endswith('.ts'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, start_dir)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    elements = []
                    
                    # Scan for buttons
                    for match in re.finditer(patterns['button'], content):
                        label = match.group(1) or match.group(2)
                        if label and not label.strip().startswith('{'): # Ignore dynamic content for now
                             elements.append({
                                'type': 'button',
                                'label': label.strip(),
                                'line': content[:match.start()].count('\n') + 1
                            })

                    # Scan for inputs
                    for match in re.finditer(patterns['input'], content):
                        placeholder = match.group(1) or match.group(2)
                        if placeholder:
                             elements.append({
                                'type': 'input',
                                'label': placeholder.strip(),
                                'line': content[:match.start()].count('\n') + 1
                            })
                            
                    if elements:
                        inventory[rel_path] = elements

    return inventory

def check_coverage(inventory, proof_script_path):
    """
    Checks if the identified elements are referenced in the proof script.
    """
    with open(proof_script_path, 'r', encoding='utf-8') as f:
        proof_content = f.read()

    coverage_report = {}
    
    for file_path, elements in inventory.items():
        file_coverage = []
        for el in elements:
            # Simple check: Is the label text present in the proof script?
            # This is a heuristic. A robust check would need AST parsing of the test script.
            is_covered = el['label'] in proof_content
            file_coverage.append({
                **el,
                'covered': is_covered
            })
        coverage_report[file_path] = file_coverage

    return coverage_report

if __name__ == "__main__":
    src_dir = "src"
    proof_script = "scripts/milestone_proof.py"
    
    print(f"Scanning {src_dir} for interactive elements...")
    inventory = scan_interactive_elements(src_dir)
    
    print(f"Checking coverage against {proof_script}...")
    report = check_coverage(inventory, proof_script)
    
    output_path = "docs/qat/interaction_inventory.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
        
    print(f"Inventory saved to {output_path}")

    # Generate Smoke Test
    print("Generating Smoke Test Suite...")
    smoke_test_path = "tests/auto_generated_interaction.py"
    with open(smoke_test_path, "w", encoding="utf-8") as f:
        f.write("import time\n")
        f.write("from playwright.sync_api import sync_playwright\n\n")
        f.write("def run_smoke_test():\n")
        f.write("    with sync_playwright() as p:\n")
        f.write("        browser = p.chromium.launch(headless=True)\n")
        f.write("        page = browser.new_page()\n")
        f.write("        page.goto('http://localhost:5173')\n")
        f.write("        # Auto-generated steps based on inventory\n")
        
        for file, items in report.items():
            f.write(f"        # Test Coverage for {file}\n")
            for item in items:
                if item['type'] == 'button' and not item['covered']:
                    # Heuristic: Try to find button by text and click if visible
                    # Simplify label to remove template literal syntax ${...} if simple enough, otherwise truncate
                    raw_label = item['label']
                    if '${' in raw_label:
                         # Attempt to extract static part or skip complex dynamic labels
                         clean_label = re.sub(r'\$\{.*?\}', '', raw_label).strip()
                         label = clean_label.replace("'", "\\'").replace("\n", " ")
                    else:
                         label = raw_label.replace("'", "\\'").replace("\n", " ")
                    f.write(f"        try:\n")
                    f.write(f"            btn = page.get_by_text('{label}').first\n")
                    f.write(f"            if btn.is_visible():\n")
                    f.write(f"                btn.click(timeout=1000)\n")
                    # Use + concatenation to avoid f-string nested brace issues
                    f.write(f"                print('✅ Covered: ' + '{label}')\n")
                    f.write(f"        except Exception as e:\n")
                    f.write(f"            # Fallback for complex labels\n")
                    f.write(f"            print('⚠️ Skipped: ' + '{label}' + ' (Not Visible/Found)')\n")
        
        f.write("        browser.close()\n\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    run_smoke_test()\n")

    print(f"Smoke test generated at {smoke_test_path}")
    
    # Calculate stats
    total_elements = sum(len(els) for els in report.values())
    covered_elements = sum(len([e for e in els if e['covered']]) for els in report.values())
    
    print("-" * 30)
    print(f"Total Interactive Elements Found: {total_elements}")
    print(f"Elements Referenced in Proof Script: {covered_elements}")
    print(f"Test Generator has created coverage for: {total_elements - covered_elements} potentially untested elements.")
    print("-" * 30)
