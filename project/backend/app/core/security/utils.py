import jwt
import uuid
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from app.domain.services.auth import PasswordService, TokenService
from app.core.configs.settings import settings

class ArgonPasswordHasher(PasswordService):
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

class JWTTokenService(TokenService):
    def create_access_token(self, user_id: uuid.UUID) -> str:
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return self._create_token(user_id, expires_delta, "access")

    def create_refresh_token(self, user_id: uuid.UUID) -> str:
        expires_delta = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        return self._create_token(user_id, expires_delta, "refresh")

    def verify_token(self, token: str) -> str:
        try:
            payload = jwt.decode(
                token, 
                settings.JWT_SECRET_KEY, 
                algorithms=[settings.JWT_ALGORITHM]
            )
            return payload.get("sub")
        except jwt.PyJWTError:
            return None

    def _create_token(self, user_id: uuid.UUID, expires_delta: timedelta, token_type: str) -> str:
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode = {
            "exp": expire,
            "sub": str(user_id),
            "type": token_type
        }
        return jwt.encode(
            to_encode, 
            settings.JWT_SECRET_KEY, 
            algorithm=settings.JWT_ALGORITHM
        )