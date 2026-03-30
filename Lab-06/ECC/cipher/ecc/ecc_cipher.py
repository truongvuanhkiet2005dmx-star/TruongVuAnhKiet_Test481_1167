import os
from ecdsa import SigningKey, VerifyingKey, NIST256p

class ECCCipher:
    def __init__(self):
        # Path relative to the lab-03/ecc folder
        self.key_dir = os.path.join(os.path.dirname(__file__), "Keys")
        self.private_path = os.path.join(self.key_dir, "private_key.pem")
        self.public_path = os.path.join(self.key_dir, "public_key.pem")

    def generate_keys(self):
        # Create private key (SigningKey) using NIST P-256 curve
        sk = SigningKey.generate(curve=NIST256p)
        vk = sk.verifying_key

        # Save keys to the Keys folder
        with open(self.private_path, "wb") as f:
            f.write(sk.to_pem())
        with open(self.public_path, "wb") as f:
            f.write(vk.to_pem())
        
        return "ECC Keys generated and saved in ecc/Keys/"

    def sign_message(self, message):
        if not os.path.exists(self.private_path):
            return None
        
        with open(self.private_path, "rb") as f:
            sk = SigningKey.from_pem(f.read())
        
        # Sign the message and return hex string for display
        signature = sk.sign(message.encode('utf-8'))
        return signature.hex()

    def verify_signature(self, message, signature_hex):
        if not os.path.exists(self.public_path):
            return False
        
        try:
            with open(self.public_path, "rb") as f:
                vk = VerifyingKey.from_pem(f.read())
            
            sig_bytes = bytes.fromhex(signature_hex)
            return vk.verify(sig_bytes, message.encode('utf-8'))
        except Exception:
            return False