"""
PRAMOD AI: Proactive Reasoning & Autonomous Multi-agent Operating Daemon
Base Agent Class
Author: Pramod Jogdand | github.com/Prem2868
© 2026 Pramod Jogdand. All rights reserved.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseAgent(ABC):
    """
    Abstract base class for all specialized agents in the PRAMOD AI ecosystem.
    """
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    async def run(self, task: str) -> Dict[str, Any]:
        """
        Execute the assigned task autonomously.
        """
        pass

    def log_action(self, action: str):
        print(f"[{self.name}] {action}")
