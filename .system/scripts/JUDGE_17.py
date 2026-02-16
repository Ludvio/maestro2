import os
import sys

def judge_phase_17():
    print("--- JUDGE PHASE 17: LABOR TOKENS ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_17_LABOR.md",
        "D (RFC)": "docs/phases/phase_17/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_17_sim.ts",
        "I (Impl)": "src/store/useLaborStore.ts",
        "UI": "src/pages/LaborDashboard.tsx"
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 17 is vertically compliant.")

judge_phase_17()
