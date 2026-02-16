import os
import sys

def judge_phase_01():
    print("--- JUDGE PHASE 01: CORE UI ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_01_UI.md",
        "D (RFC)": "docs/phases/phase_01/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_01_sim.ts",
        "I (Impl)": "src/store/useUIStore.ts",
        "UI": "src/App.tsx",
        "P (Proof)": "public/proofs/phase_01_onboarding.png"
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 01 is vertically compliant.")

judge_phase_01()
