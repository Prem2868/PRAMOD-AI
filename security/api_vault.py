"""
PRAMOD AI: Proactive Reasoning & Autonomous Multi-agent Operating Daemon
API Vault Module
Author: Pramod Jogdand | github.com/Prem2868
© 2026 Pramod Jogdand. All rights reserved.
"""

from typing import Optional
from .encryption import EncryptionManager

class APIVault:
    """
    Secure storage for API keys and sensitive credentials.
    """
    def __init__(self, master_key: str):
        self.cipher = EncryptionManager(master_key)
        self.vault = {}

    def store_key(self, service_name: str, api_key: str):
        """
        Encrypts and stores an API key.
        """
        encrypted_key = self.cipher.encrypt(api_key)
        self.vault[service_name] = encrypted_key

    def get_key(self, service_name: str) -> Optional[str]:
        """
        Retrieves and decrypts an API key.
        """
        encrypted_key = self.vault.get(service_name)
        if encrypted_key:
            return self.cipher.decrypt(encrypted_key)
        return None
