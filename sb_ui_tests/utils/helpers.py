import random
import string
from typing import Dict


def random_credentials() -> Dict[str, str]:
    def rnd(n: int = 8) -> str:
        return "".join(random.choice(string.ascii_lowercase) for _ in range(n))

    email = f"{rnd()}@example.com"
    password = rnd(12)
    name = rnd(6)
    return {"email": email, "password": password, "name": name}



