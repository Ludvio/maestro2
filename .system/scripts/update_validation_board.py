#!/usr/bin/env python3
import os
from datetime import datetime

def update_board():
    board_path = "docs/observability/VALIDATION_BOARD.md"
    if not os.path.exists(board_path):
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(board_path, 'r') as f:
        content = f.read()

    # Update all [TIMESTAMP] placeholders
    new_content = content.replace("[TIMESTAMP]", now)
    
    with open(board_path, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    update_board()
