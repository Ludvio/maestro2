import os
import glob
import json

def audit_maestro_matrix():
    total_phases = 37
    layers = ["A", "B", "D", "E", "S", "I", "UI", "F", "G", "P"]
    
    # Store Mapping: Phase -> Store Name (use[Name]Store.ts)
    STORES = {
        "01": ["UI"], "02": ["Sync"], "03": ["User"], "04": ["Sync"], "05": ["Trade"],
        "06": ["Resource"], "07": ["Sync"], "08": ["Market"], "09": ["Trade"],
        "10": ["Energy"], "11": ["Sync"], "12": ["Sync"],
        "13": ["Wspolnota"], "14": ["Harvest"], "15": ["Merit"], "16": ["Covenant"],
        "17": ["Labor"], "18": ["Help"], "19": ["World"], "20": ["Sync"], 
        "21": ["Trust", "User"], "22": ["Decay"], "36": ["Trade"], "37": ["Veche"]
    }
    
    # UI Mapping: Phase -> Page/Component Name
    PAGES = {
        "01": ["SmartFeed", "Sidebar"], "02": ["SystemMonitor"], "03": ["SystemMonitor"], 
        "04": ["SystemMonitor"], "05": ["Marketplace"], "06": ["Resources"],
        "07": ["SystemMonitor"], "08": ["CommodityPrices"], "09": ["SystemMonitor"],
        "10": ["SystemMonitor"], "11": ["PrivacySettings"], "12": ["SystemMonitor"], 
        "13": ["Commonwealth"], "14": ["HarvestDashboard"], "15": ["MeritLedger"],
        "16": ["CovenantsDashboard"], "17": ["LaborDashboard"], "18": ["SmartFeed"],
        "19": ["SystemMonitor"], "20": ["SyncMonitorHUD"], "21": ["Citizenship"], "23": ["JointProjects"],
        "36": ["Marketplace"], "37": ["Veche"]
    }

    matrix = {}

    for i in range(1, total_phases + 1):
        p = f"{i:02d}"
        phase_status = {l: "❌" for l in layers}
        
        # --- Layer A/B: ADR / Reflection ---
        if glob.glob(f"docs/decisions/ADR_{p}_*.md") or glob.glob(f"docs/decisions/ADR_{i}_*.md"):
            phase_status["A"] = "✅"
            phase_status["B"] = "✅"
            
        # --- Layer D/E/F: RFC / Contract / Red Team ---
        rfc_path = f"docs/phases/phase_{p}/LAYER_D_RFC.md"
        if os.path.exists(rfc_path):
            phase_status["D"] = "✅"
            with open(rfc_path, 'r') as f:
                content = f.read().upper()
                if "CONTRACT" in content or "LAYER E" in content: phase_status["E"] = "✅"
                if "RED TEAM" in content or "LAYER F" in content: phase_status["F"] = "✅"
        
        if glob.glob(f"docs/red-team/RED_TEAM_{p}_*.md"): phase_status["F"] = "✅"

        # --- Layer S: Simulation ---
        if os.path.exists(f"prototypes/phase_{p}_sim.ts") or os.path.exists(f"prototypes/phase_{i}_sim.ts"):
            phase_status["S"] = "✅"

        # --- Layer I: Logic/Store ---
        if p in STORES:
            for s in STORES[p]:
                if os.path.exists(f"src/store/use{s}Store.ts"):
                    phase_status["I"] = "✅"

        # --- Layer UI: Interface ---
        if p in PAGES:
            for pg in PAGES[p]:
                # Check Pages, Layout components, or Dev components
                if os.path.exists(f"src/pages/{pg}.tsx") or \
                   os.path.exists(f"src/components/layout/{pg}.tsx") or \
                   os.path.exists(f"src/components/dev/{pg}.tsx"):
                    phase_status["UI"] = "✅"

        # --- Layer G: Judge ---
        if os.path.exists(f"scripts/JUDGE_{p}.py") or os.path.exists(f"scripts/JUDGE_{i}.py"):
            phase_status["G"] = "✅"

        # --- Layer P: E2E Proof ---
        if glob.glob(f"tests/e2e/phase_{p}*.spec.ts") or glob.glob(f"tests/e2e/phase_{i}*.spec.ts"):
            phase_status["P"] = "✅"

        matrix[p] = phase_status

    # --- Print Detailed Markdown Matrix ---
    print("# MAESTRO SUPREME MATRIX (DETAILED LAYER AUDIT)\n")
    print("| Phase | A | B | D | E | S | I | UI | F | G | P | VIS (%) |")
    print("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |")
    
    total_layer_points = 0
    max_layer_points = total_phases * len(layers)

    for p, layers_data in sorted(matrix.items()):
        score = list(layers_data.values()).count("✅")
        vis = (score / len(layers)) * 100
        total_layer_points += score
        
        row = f"| {p} | " + " | ".join(layers_data[l] for l in layers) + f" | {vis:.0f}% |"
        print(row)

    overall_progress = (total_layer_points / max_layer_points) * 100
    print(f"\n**OVERALL SYSTEM INTEGRITY (VIS): {overall_progress:.1f}%**")

if __name__ == "__main__":
    audit_maestro_matrix()
