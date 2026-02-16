import os
import sys

def judge_phase_03():
    print("--- JUDGE PHASE 03: IDENTITY ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_03_IDENTITY.md",
        "D (RFC)": "docs/phases/phase_03/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_03_sim.ts",
        "I (Impl)": "src/store/useUserStore.ts"
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 03 is vertically compliant.")

judge_phase_03()
