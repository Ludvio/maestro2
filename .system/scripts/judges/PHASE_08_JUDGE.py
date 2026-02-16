# Description: Unified Phase Judge Script for Phase 08 (Retrofit).
# Orchestration: Phase 08 | Retrofit | Standard: Opus-Architect

import sys
import os

def check_file(path):
    if os.path.exists(path):
        print(f"✅ FOUND: {path}")
        return True
    else:
        print(f"❌ MISSING: {path}")
        return False

def main():
    PHASE_ID = "08"
    print(f"=== ⚖️  GROMADA PHASE {PHASE_ID} JUDGEMENT DAY ⚖️  ===")
    
    # 1. Implementation Check (Layer I)
    impl_files = [
        "src/pages/CommodityPrices.tsx",
    ]
    
    all_impl = all([check_file(f) for f in impl_files])
    
    # 2. E2E Proof Check (Layer P)
    proof_ok = check_file(f"tests/e2e/phase_{PHASE_ID}_prices.spec.ts")
    
    if all_impl and proof_ok:
        print(f"\n🎉 PHASE {PHASE_ID} IS RETROFITTED & SECURED.")
        sys.exit(0)
    else:
        print(f"\n🚨 PHASE {PHASE_ID} INCOMPLETE.")
        sys.exit(1)

if __name__ == "__main__":
    main()
