from app.domain.services.auth import PasswordService, TokenService
from app.core.security.utils import ArgonPasswordHasher, JWTTokenService

def get_password_service() -> PasswordService:
    return ArgonPasswordHasher()

def get_token_service() -> TokenService:
    return JWTTokenService()