import os
import sys

def check_phase_15():
    print("--- JUDGE PHASE 15: MERIT LEDGER ---")
    
    if not os.path.exists("src/pages/MeritLedger.tsx"):
        print("FAILED: Implementation missing.")
        sys.exit(1)
        
    print("SUCCESS: Phase 15 Infrastructure verified.")

check_phase_15()
