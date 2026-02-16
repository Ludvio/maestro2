# Description: Unified Phase Judge Script for Phase 36 (Trade Caravans).
# Orchestration: Phase 36 | Standard: Golden-Flow | Strict E2E

import sys
import os

def check_file(path, description):
    if os.path.exists(path):
        print(f"✅ FOUND: {description} -> {path}")
        return True
    else:
        print(f"❌ MISSING: {description} -> {path}")
        return False

def main():
    PHASE_ID = "36"
    print(f"=== ⚖️  GROMADA PHASE {PHASE_ID} JUDGEMENT DAY ⚖️  ===")
    
    status = True
    
    # 1. Implementation Check (Layer I)
    impl_files = [
        ("src/pages/Marketplace.tsx", "Market UI"),
        ("src/store/useTradeStore.ts", "Trade Store (Sync + Merit)"),
        ("src/App.tsx", "Routing"),
    ]
    
    if not all([check_file(f[0], f[1]) for f in impl_files]):
        status = False
    
    # 2. Security Check (Layer F)
    if not check_file(f"tests/red_team/phase_{PHASE_ID}_attack.py", "Red Team Spec"):
        status = False
        
    # 3. E2E Proof Check (Layer P)
    if not check_file(f"tests/e2e/phase_{PHASE_ID}_trade.spec.ts", "Playwright Proof"):
        status = False
        
    if status:
        print(f"\n🎉 PHASE {PHASE_ID} IS SECURE & READY.")
        sys.exit(0)
    else:
        print(f"\n🚨 PHASE {PHASE_ID} INCOMPLETE. MISSING CRITICAL LAYERS.")
        sys.exit(1)

if __name__ == "__main__":
    main()
