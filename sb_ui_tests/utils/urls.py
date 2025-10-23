import os

BASE_URL = os.getenv("SB_BASE_URL", "https://stellarburgers.education-services.ru").rstrip("/")
API_BASE = os.getenv("SB_API_URL", BASE_URL).rstrip("/")

# API endpoints
AUTH_REGISTER = f"{API_BASE}/api/auth/register"
AUTH_LOGIN = f"{API_BASE}/api/auth/login"
AUTH_USER = f"{API_BASE}/api/auth/user"
INGREDIENTS = f"{API_BASE}/api/ingredients"
ORDERS = f"{API_BASE}/api/orders"



