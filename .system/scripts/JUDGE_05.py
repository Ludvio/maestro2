import os
import sys

def judge_phase_05():
    print("--- JUDGE PHASE 05: POOLING ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_05_POOLS.md",
        "D (RFC)": "docs/phases/phase_05/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_05_sim.ts",
        "I (Impl)": "src/store/useTradeStore.ts" 
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 05 is vertically compliant.")

judge_phase_05()
