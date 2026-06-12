"""
PRAMOD AI: Proactive Reasoning & Autonomous Multi-agent Operating Daemon
Short-term Memory Module
Author: Pramod Jogdand | github.com/Prem2868
© 2026 Pramod Jogdand. All rights reserved.
"""

from typing import List, Any

class ShortTermMemory:
    """
    Manages transient context and session-specific data.
    """
    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        self.buffer = []

    def add(self, item: Any):
        if len(self.buffer) >= self.capacity:
            self.buffer.pop(0)
        self.buffer.append(item)

    def get_context(self) -> List[Any]:
        return self.buffer

    def clear(self):
        self.buffer = []
