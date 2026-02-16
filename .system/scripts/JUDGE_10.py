import os
import sys

def judge_phase_10():
    print("--- JUDGE PHASE 10: ENERGY MANAGEMENT ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_10_TRENDS.md",
        "D (RFC)": "docs/phases/phase_10/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_10_sim.ts",
        "I (Impl)": "src/store/useEnergyStore.ts"
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 10 is vertically compliant.")

judge_phase_10()
