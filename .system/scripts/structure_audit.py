import os

PILLARS = {
    "00_CORE": ["01", "02", "03", "04", "20"],
    "01_HOUSEHOLD": ["06", "14", "22", "24", "26", "28"],
    "02_MARKET": ["05", "08", "09", "10", "17", "23", "27", "31", "36"],
    "03_HEARTH": ["13", "15", "18", "25", "29", "30", "33", "35"],
    "04_ASSEMBLY": ["11", "12", "16", "19", "21", "32", "34", "37"]
}

def audit():
    print("🛡️ GROMADA STRUCTURE AUDIT (Four Pillars)")
    print("-" * 40)
    
    total_phases = 37
    mapped = 0
    missing = []

    for pillar, phases in PILLARS.items():
        print(f"\n[{pillar}]")
        for p in phases:
            path = f"docs/domains/{pillar}/phase_{p}"
            legacy_path = f"docs/phases/phase_{p}"
            
            if os.path.exists(path):
                print(f"  ✅ Phase {p}: Organized")
                mapped += 1
            elif os.util.path.exists(legacy_path) if hasattr(os, 'util') else os.path.exists(legacy_path):
                print(f"  ⚠️  Phase {p}: Legacy Location")
            else:
                print(f"  ❌ Phase {p}: Mission Critical (Missing)")
                missing.append(p)

    print("-" * 40)
    print(f"Progress: {mapped}/{total_phases} phases organized into Pillars.")
    print(f"Compliance: {(mapped/total_phases)*100:.1f}%")

if __name__ == "__main__":
    audit()
