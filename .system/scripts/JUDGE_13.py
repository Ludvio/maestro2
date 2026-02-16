import os
import sys

def check_phase_13():
    print("--- JUDGE PHASE 13: COMMONWEALTH ---")
    
    required = [
        "docs/decisions/ADR_13_COMMONWEALTH.md",
        "docs/phases/phase_13/LAYER_D_RFC.md",
        "docs/idempotency_contracts/phase_13_commonwealth.json",
        "src/store/useWspolnotaStore.ts"
    ]
    
    for f in required:
        if not os.path.exists(f):
            print(f"FAILED: Missing {f}")
            sys.exit(1)

    print("SUCCESS: Phase 13 Infrastructure is valid.")

check_phase_13()
