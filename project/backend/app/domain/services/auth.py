import uuid
from abc import ABC, abstractmethod

class PasswordService(ABC):
    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        pass
        
    @abstractmethod
    def hash(self, password: str) -> str:
        pass

class TokenService(ABC):
    @abstractmethod
    def create_access_token(self, user_id: uuid.UUID) -> str:
        pass

    @abstractmethod
    def create_refresh_token(self, user_id: uuid.UUID) -> str:
        pass 
    
    @abstractmethod
    def verify_token(self, token: str) -> str:
        pass