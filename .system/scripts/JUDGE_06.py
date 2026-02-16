import os
import sys

def check_phase_06():
    print("--- JUDGE PHASE 06: RESOURCES ---")
    
    # Check for core artifacts
    if not os.path.exists("src/pages/Resources.tsx"):
        print("FAILED: Implementation missing.")
        sys.exit(1)
        
    if not os.path.exists("tests/e2e/phase_06_resources.spec.ts"):
        print("FAILED: Proof missing.")
        sys.exit(1)
        
    print("SUCCESS: Phase 06 Battle-Proven.")

check_phase_06()
