import re
import sys
import os

def check_sidebar_integrity():
    sidebar_path = "src/components/layout/Sidebar.tsx"
    if not os.path.exists(sidebar_path):
        print("❌ Error: Sidebar.tsx not found!")
        return False

    with open(sidebar_path, 'r') as f:
        content = f.read()

    # Define the 4 Pillars as per engineering standard
    pillars = ["Gospodarstwo", "Rynek", "Ognisko", "Wiec"]
    max_items = 7
    
    # Extract sections from Sidebar.tsx
    # Looking for: title: "SectionName", items: [...]
    section_pattern = re.compile(r'title:\s*"([^"]+)",\s*items:\s*\[([^\]]+)\]', re.DOTALL)
    sections = section_pattern.findall(content)

    print("🛡️  GROMADA UX INTEGRITY AUDIT")
    print("-" * 30)
    
    all_ok = True
    found_pillars = [s[0] for s in sections]

    # 1. Check if all pillars are present
    for p in pillars:
        if p not in found_pillars:
            print(f"❌ Missing Pillar: {p}")
            all_ok = False
        else:
            # 2. Check cognitive load per pillar
            items_text = next(s[1] for s in sections if s[0] == p)
            # Count occurrences of { id: ... }
            item_count = items_text.count('{ id:')
            
            status = "✅" if item_count <= max_items else "🔥 OVERLOAD"
            print(f"{status} {p}: {item_count}/{max_items} items")
            
            if item_count > max_items:
                print(f"   └─ ALERT: Cognitive load too high for '{p}'! Consolidate features.")
                all_ok = False

    # 3. Check for total chaos (too many top level sections)
    if len(sections) > 6:
        print(f"❌ Warning: Too many navigation sections ({len(sections)}). Keep it to the Four Pillars.")
        all_ok = False

    print("-" * 30)
    if all_ok:
        print("🟢 UX STATUS: COHERENT")
        return True
    else:
        print("🔴 UX STATUS: FRAGMENTED")
        return False

if __name__ == "__main__":
    if not check_sidebar_integrity():
        sys.exit(1)
    sys.exit(0)
