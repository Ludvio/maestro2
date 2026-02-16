import os
import sys

def judge_phase_02():
    print("--- JUDGE PHASE 02: DATA MODELS ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_02_DATA_MODELS.md",
        "D (RFC)": "docs/phases/phase_02/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_02_sim.ts",
        "I (Impl)": "src/store/useSyncStore.ts",
        "P (Proof)": "tests/e2e/phase_20_sync.spec.ts" # Phase 02 is proven by Sync E2E
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 02 is vertically compliant.")

judge_phase_02()
