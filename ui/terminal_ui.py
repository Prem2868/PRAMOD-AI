"""
PRAMOD AI: Proactive Reasoning & Autonomous Multi-agent Operating Daemon
Terminal User Interface
Author: Pramod Jogdand | github.com/Prem2868
© 2026 Pramod Jogdand. All rights reserved.
"""

import os
from typing import List, Dict, Any

class TerminalUI:
    """
    Handles terminal-based interaction for PRAMOD AI.
    """
    def display_banner(self):
        banner = r"""
  ██████╗ ██████╗  █████╗ ███╗   ███╗ ██████╗ ██████╗      █████╗ ██╗
  ██╔══██╗██╔══██╗██╔══██╗████╗ ████║██╔═══██╗██╔══██╗    ██╔══██╗██║
  ██████╔╝██████╔╝███████║██╔████╔██║██║   ██║██║  ██║    ███████║██║
  ██╔═══╝ ██╔══██╗██╔══██║██║╚██╔╝██║██║   ██║██║  ██║    ██╔══██║██║
  ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║╚██████╔╝██████╔╝    ██║  ██║██║
  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═════╝     ╚═╝  ╚═╝╚═╝
  Proactive Reasoning & Autonomous Multi-agent Operating Daemon
  Built by Pramod Jogdand | github.com/Prem2868
        """
        print(banner)

    def log(self, message: str, level: str = "INFO"):
        print(f"[{level}] {message}")

    async def get_input(self, prompt: str) -> str:
        return input(f"PRAMOD AI > {prompt}")

    def display_plan(self, plan: List[Dict[str, Any]]):
        print("\n--- STRATEGIC PLAN ---")
        for step in plan:
            print(f"{step['id']}. [{step['agent'].upper()}] {step['task']}")
        print("----------------------\n")

    def display_results(self, results: List[Dict[str, Any]]):
        print("\n--- EXECUTION RESULTS ---")
        for res in results:
            print(f"Step {res['step']}: {res['status']} - {res['output']}")
        print("-------------------------\n")
