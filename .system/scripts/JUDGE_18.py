import os
import sys

def judge_phase_18():
    print("--- JUDGE PHASE 18: MUTUAL AID ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_18_HELP.md",
        "D (RFC)": "docs/phases/phase_18/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_18_sim.ts",
        "I (Impl)": "src/store/useHelpStore.ts",
        "UI": "src/components/domain/feed/HelpSignalCard.tsx",
        "P (Proof)": "tests/e2e/phase_18.spec.ts"
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 18 is vertically compliant.")

judge_phase_18()
