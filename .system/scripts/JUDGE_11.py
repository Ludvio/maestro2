import os
import sys

def judge_phase_11():
    print("--- JUDGE PHASE 11: SPATIAL PRIVACY ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_11_PRIVACY.md",
        "D (RFC)": "docs/phases/phase_11/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_11_sim.ts",
        "UI": "src/pages/PrivacySettings.tsx"
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 11 is vertically compliant.")

judge_phase_11()
