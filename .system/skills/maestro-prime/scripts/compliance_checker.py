
import os
import sys
import re

# Configuration
CONSTITUTION_PATH = "docs/constitution/GROMADA_PRINCIPLES.md"
TECH_STACK_PATH = "docs/templates/STANDARD_TECH_STACK.md"

def check_phase_compliance(phase_id, phase_name):
    """
    Simulates a 'Compliance Officer' audit.
    Checks if artifacts reference the Constitution and Tech Stack.
    """
    print(f"[*] Auditing Phase {phase_id} for Compliance...")
    
    # Check Layer 1: Business Milestone (A)
    # Note: Milestone file name might be PHASE_NAME or ID_NAME
    milestone_path = f"docs/phases/MILESTONE_{phase_id}_{phase_name.upper()}.md"
    if not os.path.exists(milestone_path):
        # Retry with just ID if name differs
        found = False
        for f in os.listdir("docs/phases"):
            if f"MILESTONE_{phase_id}" in f:
                milestone_path = f"docs/phases/{f}"
                found = True
                break
        if not found:
            print(f"[!] FAILED: Milestone file missing for Phase {phase_id}.")
            return False
        
    print(f"[*] Checking {milestone_path}...")
    with open(milestone_path, 'r') as f:
        content = f.read()
        if "Constitutional Check" not in content and "Article I" not in content and "GROMADA_PRINCIPLES.md" not in content:
            print(f"[!] FAILED: Milestone must reference Constitution.")
            return False
            
    # Check Layer 4: Tech Plan (D)
    tech_path = f"docs/implementation_plans/phase_{phase_id}_{phase_name}.md"
    if not os.path.exists(tech_path):
        print(f"[!] FAILED: Implementation Plan missing at {tech_path}.")
        return False
        
    with open(tech_path, 'r') as f:
        content = f.read()
        # Loose check for tech stack mentions
        if "React" not in content and "Standard" not in content and "Zustand" not in content:
             print(f"[!] WARN: Tech Plan may not reference Standard Tech Stack.")
            
    print(f"[*] Phase {phase_id} Compliance Audit Passed.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 compliance_checker.py [ID] [NAME]")
        sys.exit(1)
    success = check_phase_compliance(sys.argv[1], sys.argv[2])
    if not success:
        sys.exit(1)
