import os
import sys

def check_ui_integrity():
    print("--- JUDGE UI INTEGRITY (Phases 08, 18, 23) ---")
    
    files = [
        "src/pages/CommodityPrices.tsx",
        "src/pages/JointProjects.tsx",
        "src/components/domain/feed/HelpSignalCard.tsx"
    ]
    
    for f in files:
        if not os.path.exists(f):
            print(f"FAILED: {f} not found!")
            sys.exit(1)
            
    # Check if they are integrated in App.tsx
    with open("src/App.tsx", "r") as app:
        content = app.read()
        if "JointProjects" not in content:
            print("FAILED: JointProjects not in App.tsx")
            sys.exit(1)

    print("SUCCESS: UI Layers for Batch #11 are correctly integrated.")

check_ui_integrity()
