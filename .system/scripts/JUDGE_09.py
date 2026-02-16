import os
import sys

def judge_phase_09():
    print("--- JUDGE PHASE 09: YIELD ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_09_ECONOMICS.md",
        "D (RFC)": "docs/phases/phase_09/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_09_sim.ts",
        "I (Impl)": "src/store/useTradeStore.ts" 
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 09 is vertically compliant.")

judge_phase_09()
