import os
import sys

def judge_phase_19():
    print("--- JUDGE PHASE 19: ENVIRONMENTAL CYCLES ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_19_WEATHER.md",
        "D (RFC)": "docs/phases/phase_19/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_19_sim.ts",
        "I (Impl)": "src/store/useWorldStore.ts"
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 19 is vertically compliant.")

judge_phase_19()
