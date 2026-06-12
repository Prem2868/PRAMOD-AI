"""
PRAMOD AI: Proactive Reasoning & Autonomous Multi-agent Operating Daemon
Main Entry Point
Author: Pramod Jogdand | github.com/Prem2868
© 2026 Pramod Jogdand. All rights reserved.
"""

import asyncio
import sys
from core.brain import Brain
from core.health_monitor import HealthMonitor
from ui.terminal_ui import TerminalUI

class PramodAI:
    def __init__(self):
        self.name = "PRAMOD AI"
        self.author = "Pramod Jogdand"
        self.tagline = "Not just an assistant. An AI that thinks, plans, acts, and evolves."
        self.brain = Brain()
        self.health_monitor = HealthMonitor()
        self.ui = TerminalUI()

    async def run(self):
        """
        Autonomous Engine loop:
        Goal -> Plan -> Execute -> Monitor -> Improve -> Repeat
        """
        self.ui.display_banner()
        self.ui.log(f"Initializing {self.name} system...")
        
        if not self.health_monitor.check_systems():
            self.ui.log("System health check failed. Shutting down.", level="ERROR")
            sys.exit(1)

        self.ui.log("All systems operational. Starting autonomous loop.")
        
        while True:
            try:
                # 1. Goal Acquisition
                goal = await self.ui.get_input("Enter your goal: ")
                if goal.lower() in ["exit", "quit", "shutdown"]:
                    break

                # 2. Planning
                self.ui.log(f"Architecting plan for: {goal}")
                plan = await self.brain.plan(goal)
                self.ui.display_plan(plan)

                # 3. Execution
                self.ui.log("Executing autonomous tasks...")
                results = await self.brain.execute(plan)
                
                # 4. Monitoring
                self.ui.log("Monitoring execution results and system state...")
                feedback = self.health_monitor.analyze_performance(results)
                
                # 5. Improvement
                self.ui.log("Learning from execution for future optimizations...")
                await self.brain.learn(goal, plan, results, feedback)
                
                # 6. Output Result
                self.ui.display_results(results)

            except Exception as e:
                self.ui.log(f"An unexpected error occurred in the loop: {e}", level="ERROR")
                # Attempt self-healing
                await self.health_monitor.self_heal(e)

        self.ui.log(f"Shutting down {self.name}. Goodbye.")

if __name__ == "__main__":
    app = PramodAI()
    try:
        asyncio.run(app.run())
    except KeyboardInterrupt:
        print(f"\n[PRAMOD AI] Process terminated by user.")
