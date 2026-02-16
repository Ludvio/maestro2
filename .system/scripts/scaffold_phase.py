import os
import sys
import json
import shutil

TEMPLATE_PATH = "/home/lu/Documents/system/templates/MANIFEST_TEMPLATE.json"
BASE_DOCS = "docs/domains"

PILLAR_MAP = {
    "00": "00_CORE",
    "01": "01_HOUSEHOLD",
    "02": "02_MARKET",
    "03": "03_HEARTH",
    "04": "04_ASSEMBLY"
}

def scaffold(phase_id, pillar_key, name):
    pillar = PILLAR_MAP.get(pillar_key)
    if not pillar:
        print(f"Error: Invalid pillar key {pillar_key}. Use 00-04.")
        return

    phase_dir = os.path.join(BASE_DOCS, pillar, f"phase_{phase_id}_{name}")
    print(f"🏗️  Scaffolding Phase {phase_id} in {pillar}...")

    # Create directories
    os.makedirs(os.path.join(phase_dir, "tests/red_team"), exist_ok=True)
    os.makedirs(os.path.join(phase_dir, "tests/evals"), exist_ok=True)

    # Prepare Manifest
    with open(TEMPLATE_PATH, 'r') as f:
        manifest = json.load(f)

    manifest["domain"] = pillar.split('_')[1]
    manifest["description"] = f"Automatic scaffold for {name}"
    
    with open(os.path.join(phase_dir, "MANIFEST.json"), 'w') as f:
        json.dump(manifest, f, indent=4)

    # Create dummy files
    files = [
        "LAYER_D_RFC.md",
        "LAYER_F_RED_TEAM.md",
        "LAYER_E_CONTRACT.json"
    ]
    for filename in files:
        filepath = os.path.join(phase_dir, filename)
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                f.write(f"# {filename} for Phase {phase_id}\nInitialized by Scaffolder.")

    print(f"✅ Created: {phase_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 scaffold_phase.py [ID] [PILLAR_KEY] [NAME]")
        print("Example: python3 scaffold_phase.py 38 02 resource_hub")
    else:
        scaffold(sys.argv[1], sys.argv[2], sys.argv[3])
