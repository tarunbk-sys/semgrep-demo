import hashlib

# INTENTIONALLY VULNERABLE: hardcoded secret and weak hash for Semgrep demo purposes only.
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()
