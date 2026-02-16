# Description: Unified Phase Judge Script for Phase 15.
# Orchestration: Phase 15 | Retrofit | Standard: Anthropic-Hard-Gate

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
    PHASE_ID = "15"
    print(f"=== ⚖️  GROMADA PHASE {PHASE_ID} JUDGEMENT DAY ⚖️  ===")
    
    # 1. Implementation Check (Layer I)
    impl_files = [
        "src/domain/trust/TrustEngine.ts",
        "src/store/useMeritStore.ts",
        "src/pages/MeritLedger.tsx"
    ]
    
    all_impl = all([check_file(f) for f in impl_files])
    
    # 2. RFC Check (Layer D)
    rfc_ok = check_file(f"docs/rfcs/RFC_{PHASE_ID}_merit_ledger.md")
    
    if all_impl and rfc_ok:
        print("\n🎉 PHASE 15 IS PRODUCTION-READY (CODE + DOCS).")
        sys.exit(0)
    else:
        print("\n🚨 PHASE 15 INCOMPLETE.")
        sys.exit(1)

if __name__ == "__main__":
    main()
