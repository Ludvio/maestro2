import os
import sys

def judge_phase_04():
    print("--- JUDGE PHASE 04: DISCOVERY ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_04_NETWORKING.md",
        "D (RFC)": "docs/phases/phase_04/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_04_sim.ts",
        "I (Impl)": "src/store/useSyncStore.ts" 
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 04 is vertically compliant.")

judge_phase_04()
