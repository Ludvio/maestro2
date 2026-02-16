import os
import sys

def judge_phase_16():
    print("--- JUDGE PHASE 16: COVENANTS ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_16_COVENANTS.md",
        "D (RFC)": "docs/phases/phase_16/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_16_sim.ts",
        "I (Impl)": "src/store/useCovenantStore.ts",
        "UI": "src/pages/CovenantsDashboard.tsx"
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 16 is vertically compliant.")

judge_phase_16()
