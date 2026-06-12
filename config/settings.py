"""
PRAMOD AI: Proactive Reasoning & Autonomous Multi-agent Operating Daemon
Global Settings
Author: Pramod Jogdand | github.com/Prem2868
© 2026 Pramod Jogdand. All rights reserved.
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Central configuration for PRAMOD AI.
    """
    PROJECT_NAME = "PRAMOD AI"
    AUTHOR = "Pramod Jogdand"
    GITHUB_URL = "github.com/Prem2868"
    
    # Core Engine Settings
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    MASTER_KEY = os.getenv("PRAMOD_MASTER_KEY", "default-secret-key")
    
    # Integration Keys
    NOTION_API_KEY = os.getenv("NOTION_API_KEY")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    
    # Agent Settings
    DEFAULT_MODEL = "PRAMOD-REASONING-v1"
    AGENT_TIMEOUT = 300
