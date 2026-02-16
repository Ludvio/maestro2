import os
import glob

# Constants for the Supreme Architecture Phases (1-37)
TOTAL_PHASES = 37
LAYERS = ["A", "B", "D", "E", "L", "S", "I", "U", "F", "G", "P"]

# ANSI Colors
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"
BOLD = "\033[1m"
GRAY = "\033[90m"

def get_status():
    matrix = {}
    
    # Heuristic Mappings
    STORES = {
        "01": ["UI"], "02": ["Sync"], "03": ["User"], "04": ["Sync"], "05": ["Trade"],
        "06": ["Resource"], "07": ["Sync"], "08": ["Market"], "09": ["Trade"], "10": ["Energy"],
        "11": ["Sync"], "12": ["Sync"],
        "13": ["Wspolnota"], "14": ["Harvest"], "15": ["Merit"], "16": ["Covenant"],
        "17": ["Labor"], "18": ["Help"], "19": ["World"], "20": ["Sync"], 
        "21": ["Trust", "User"], "22": ["Decay"], "23": ["JointProjects"], "24": ["Refining"], 
        "25": ["Weather"], "26": ["Circular"], "27": ["Bridge"], "28": ["Storage"],
        "29": ["Forecast"], "30": ["Library"], "31": ["Skill"], "32": ["Law"],
        "33": ["Ritual"],
        "36": ["Trade"], "37": ["Veche"]
    }
    
    PAGES = {
        "01": ["SmartFeed", "Sidebar"], "02": ["SystemMonitor"], "03": ["SystemMonitor"], 
        "04": ["SystemMonitor"], "05": ["Marketplace"], "06": ["Resources"],
        "07": ["SystemMonitor"], "08": ["CommodityPrices"], "09": ["SystemMonitor"],
        "10": ["SystemMonitor"], "11": ["PrivacySettings"], "12": ["SystemMonitor"], 
        "13": ["Commonwealth"], "14": ["HarvestDashboard"], "15": ["MeritLedger"],
        "16": ["CovenantsDashboard"], "17": ["LaborDashboard"], "18": ["SmartFeed"],
        "19": ["SystemMonitor"], "20": ["SyncMonitorHUD"], "21": ["Nationality"], "22": ["DecayMonitorHUD"], "23": ["JointProjects"], "24": ["Refinery"],
        "26": ["CircularDashboard"], "27": ["BridgeDashboard"], "28": ["StorageManager"],
        "29": ["ForecastDashboard"], "30": ["LibraryDashboard"], "31": ["SkillMarket"], "32": ["LawBook"],
        "33": ["RitualDashboard"],
        "36": ["Marketplace"], "37": ["Veche"]
    }

    for i in range(1, TOTAL_PHASES + 1):
        p = f"{i:02d}"
        matrix[p] = {l: False for l in LAYERS}
        
        # A/B: ADR
        if glob.glob(f"docs/decisions/ADR_{p}_*.md") or glob.glob(f"docs/decisions/ADR_{i}_*.md"):
            matrix[p]["A"] = matrix[p]["B"] = True
            
        # D/E/F: RFC/Contract/RedTeam
        rfc = f"docs/phases/phase_{p}/LAYER_D_RFC.md"
        if os.path.exists(rfc):
            matrix[p]["D"] = True
            with open(rfc, 'r') as f:
                c = f.read().upper()
                if "CONTRACT" in c or "LAYER E" in c: matrix[p]["E"] = True
                if "RED TEAM" in c or "LAYER F" in c: matrix[p]["F"] = True
                if "SYSTEMIC LOOPS" in c or "SYSTEMIC ARCHITECTURE" in c: matrix[p]["L"] = True
        
        # L: Loop Integration (Store check)
        if p in STORES:
            for s in STORES[p]:
                store_file = f"src/store/use{s}Store.ts"
                if os.path.exists(store_file):
                    with open(store_file, 'r') as f:
                        content = f.read()
                        # Check if it imports other stores (integration)
                        if "from './use" in content or "from '../store/use" in content:
                            matrix[p]["L"] = True

        if glob.glob(f"docs/red-team/RED_TEAM_{p}_*.md"): matrix[p]["F"] = True

        # S: Simulation
        if os.path.exists(f"prototypes/phase_{p}_sim.ts") or os.path.exists(f"prototypes/phase_{i}_sim.ts"):
            matrix[p]["S"] = True

        # I: Logic (Store)
        if p in STORES:
            for s in STORES[p]:
                if os.path.exists(f"src/store/use{s}Store.ts"):
                    matrix[p]["I"] = True

        # U: UI (Page)
        if p in PAGES:
            for pg in PAGES[p]:
                if os.path.exists(f"src/pages/{pg}.tsx") or \
                   os.path.exists(f"src/components/layout/{pg}.tsx") or \
                   os.path.exists(f"src/components/dev/{pg}.tsx"):
                    matrix[p]["U"] = True

        # G: Judge
        if os.path.exists(f"scripts/JUDGE_{p}.py") or os.path.exists(f"scripts/JUDGE_{i}.py"):
            matrix[p]["G"] = True

        # P: Proof (E2E)
        if glob.glob(f"tests/e2e/phase_{p}*.spec.ts") or glob.glob(f"tests/e2e/phase_{i}*.spec.ts"):
            # Real Proof Check: Must not be empty
            p_path = glob.glob(f"tests/e2e/phase_{p}*.spec.ts")[0] if glob.glob(f"tests/e2e/phase_{p}*.spec.ts") else ""
            if p_path and os.path.getsize(p_path) > 100:
                matrix[p]["P"] = True

    return matrix

def print_grid(matrix):
    print(f"\n{BOLD}MAESTRO SUPREME GRID{RESET} | Layers: {GRAY}A B D E S I U F G P{RESET}")
    print(f"{GRAY}------------------------------------------{RESET}")
    
    summary_total = 0
    summary_complete = 0

    for p, layers in sorted(matrix.items()):
        line = f"{BOLD}{p}{RESET} | "
        for l in LAYERS:
            char = "■" if layers[l] else "□"
            color = GREEN if layers[l] else RED
            line += f"{color}{char}{RESET} "
        
        score = list(layers.values()).count(True)
        pct = (score / len(LAYERS)) * 100
        line += f"| {BOLD}{pct:>3.0f}%{RESET}"
        print(line)
        
        summary_total += len(LAYERS)
        summary_complete += score
        
    total_pct = (summary_complete / summary_total) * 100
    print(f"{GRAY}------------------------------------------{RESET}")
    print(f"{BOLD}TOTAL INTEGRITY: {GREEN if total_pct > 50 else RED}{total_pct:.1f}%{RESET}\n")

if __name__ == "__main__":
    print_grid(get_status())
