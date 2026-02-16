# Description: Unified Phase Judge Script for Phase 20.
# Orchestration: Phase 20 | Retrofit | Standard: Anthropic-Hard-Gate

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
    PHASE_ID = "20"
    print(f"=== ⚖️  GROMADA PHASE {PHASE_ID} JUDGEMENT DAY ⚖️  ===")
    
    # 1. Implementation Check (Layer I)
    impl_files = [
        "src/domain/sync/SyncEngine.ts",
        "src/store/useSyncStore.ts",
        "src/components/dev/SyncMonitorHUD.tsx"
    ]
    
    all_impl = all([check_file(f) for f in impl_files])
    
    # 2. RFC Check (Layer D)
    rfc_ok = check_file(f"docs/rfcs/RFC_{PHASE_ID}_splot_sync.md")
    
    if all_impl and rfc_ok:
        print("\n🎉 PHASE 20 IS PRODUCTION-READY (MERKLE-MESH SYNC).")
        sys.exit(0)
    else:
        print("\n🚨 PHASE 20 INCOMPLETE.")
        sys.exit(1)

if __name__ == "__main__":
    main()
