import os
import sys

# Orchestration: Phase 25 | Layer G (Judge)
# Mandate: Automated Vertical Compliance Check for Seasonal Rhythms.

def check_file(path, label):
    if os.path.exists(path):
        print(f"✅ {label} found: {path}")
        return True
    else:
        print(f"❌ {label} MISSING: {path}")
        return False

def check_line_count(path, min_lines):
    if not os.path.exists(path): return False
    with open(path, 'r') as f:
        count = sum(1 for _ in f)
    if count >= min_lines:
        print(f"✅ {path} meets size requirement ({count} lines).")
        return True
    else:
        print(f"❌ {path} TOO SHORT ({count} < {min_lines} lines).")
        return False

def run_audit():
    print("⚖️ AUDITING PHASE 25 (SUPREME ARCHITECTURE STANDARD)...")
    
    complianceIndices = [
        check_line_count("docs/phases/phase_25/LAYER_D_RFC.md", 300),
        check_file("src/contracts/Phase25Contract.ts", "Contract"),
        check_file("src/store/useWeatherStore.ts", "Store"),
        check_file("prototypes/phase_25_sim.ts", "Simulation"),
        check_file("src/components/dev/WeatherHUD.tsx", "UI HUD"),
        check_file("tests/e2e/phase_25_weather.spec.ts", "Proof (E2E)"),
        check_file("prototypes/phase_25_fuzzer.js", "Fuzzer")
    ]
    
    score = sum(complianceIndices) / len(complianceIndices) * 100
    print(f"\n--- AUDIT COMPLETE: {score:.1f}% COMPLIANCE ---")
    
    if score == 100:
        print("🏆 PHASE 25 VERIFIED: SUPREME STATUS ACHIEVED.")
        return 0
    else:
        print("⚠️ PHASE 25 INCOMPLETE: Correct violations before deployment.")
        return 1

if __name__ == "__main__":
    sys.exit(run_audit())
