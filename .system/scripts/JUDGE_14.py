import os
import sys

def judge_phase_14():
    print("--- JUDGE PHASE 14: HARVEST CYCLES ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_14_PRODUCTION.md",
        "D (RFC)": "docs/phases/phase_14/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_14_sim.ts",
        "I (Impl)": "src/store/useHarvestStore.ts",
        "P (Proof)": "tests/e2e/phase_14.spec.ts"
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 14 is vertically compliant.")

judge_phase_14()
