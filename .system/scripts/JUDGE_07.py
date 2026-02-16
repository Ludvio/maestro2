import os
import sys

def judge_phase_07():
    print("--- JUDGE PHASE 07: STORAGE ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_07_STORAGE.md",
        "D (RFC)": "docs/phases/phase_07/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_07_sim.ts",
        "I (Impl)": "src/store/useSyncStore.ts" 
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 07 is vertically compliant.")

judge_phase_07()
