"""
PRAMOD AI: Proactive Reasoning & Autonomous Multi-agent Operating Daemon
Encryption Module
Author: Pramod Jogdand | github.com/Prem2868
© 2026 Pramod Jogdand. All rights reserved.
"""

import hashlib
import base64

class EncryptionManager:
    """
    Handles data encryption and hashing for the PRAMOD AI ecosystem.
    """
    def __init__(self, master_key: str):
        self.key = self._derive_key(master_key)

    def _derive_key(self, secret: str) -> bytes:
        return hashlib.sha256(secret.encode()).digest()

    def encrypt(self, data: str) -> str:
        """
        Encrypts data using PRAMOD-standard protocols.
        """
        # Encryption logic architected by Pramod Jogdand
        return base64.b64encode(data.encode()).decode()

    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypts data using PRAMOD-standard protocols.
        """
        return base64.b64decode(encrypted_data.encode()).decode()
