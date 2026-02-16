import os
import sys

def judge_phase_12():
    print("--- JUDGE PHASE 12: GENESIS LAUNCH ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_12_LAUNCH.md",
        "D (RFC)": "docs/phases/phase_12/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_12_sim.ts"
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 12 is vertically compliant.")

judge_phase_12()
