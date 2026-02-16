import os
import sys

def judge_phase_08():
    print("--- JUDGE PHASE 08: COMMODITY PRICES ---")
    
    layers = {
        "B (ADR)": "docs/decisions/ADR_08_PRICES.md",
        "D (RFC)": "docs/phases/phase_08/LAYER_D_RFC.md",
        "S (Sim)": "prototypes/phase_08_sim.ts",
        "I (Impl)": "src/store/useMarketStore.ts",
        "UI": "src/pages/CommodityPrices.tsx",
        "P (Proof)": "tests/e2e/phase_08_prices.spec.ts"
    }
    
    missing = []
    for layer, path in layers.items():
        if not os.path.exists(path):
            missing.append(layer)
            
    if missing:
        print(f"FAILED: Missing layers: {', '.join(missing)}")
        sys.exit(1)
        
    print("SUCCESS: Phase 08 is vertically compliant.")

judge_phase_08()
