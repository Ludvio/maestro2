#!/usr/bin/env python3
import re
import os
import json
from typing import List, Dict

def extract_invariants(plan_path: str) -> List[str]:
    """Extracts invariant names from the Gold Standard section of a markdown file."""
    invariants = []
    if not os.path.exists(plan_path):
        return []
    
    with open(plan_path, 'r') as f:
        content = f.read()
        
    # Look for the section after 🛡️ Invariants
    match = re.search(r"## 🛡️ Invariants \(The Unbreakables\)(.*?)##", content, re.DOTALL)
    if match:
        section = match.group(1)
        # Find lines starting with - **Name**:
        items = re.findall(r"- \*\*([^*]+)\*\*", section)
        invariants.extend([item.strip() for item in items])
        
    return invariants

def check_coverage():
    docs_dir = "docs/implementation_plans"
    manifest_path = "public/proofs/manifest.json"
    
    if not os.path.exists(manifest_path):
        print("Error: Run validation first to generate manifest.json")
        return

    with open(manifest_path, 'r') as f:
        report = json.load(f)

    actual_invariants = [inv["name"] for inv in report.get("invariants_checked", [])]
    
    status_report = []
    
    for filename in sorted(os.listdir(docs_dir)):
        if filename.endswith(".md"):
            phase_match = re.search(r"phase_(\d+)", filename)
            if not phase_match: continue
            
            phase_id = phase_match.group(1)
            # Only check phases that have been "implemented" in the proof engine or validation board
            # For now, we check all, but we care most about 01-04
            
            plan_invariants = extract_invariants(os.path.join(docs_dir, filename))
            if not plan_invariants: continue
            
            for inv in plan_invariants:
                status = "✅" if inv in actual_invariants else "❌"
                status_report.append({
                    "phase": phase_id,
                    "invariant": inv,
                    "status": "PASS" if status == "✅" else "MISSING",
                    "plan": filename
                })

    # Output to a coverage manifest for the HUD
    coverage_path = "public/proofs/coverage.json"
    with open(coverage_path, 'w') as f:
        json.dump(status_report, f, indent=2)
    
    print(f"Coverage check complete. Saved to {coverage_path}")

if __name__ == "__main__":
    check_coverage()
