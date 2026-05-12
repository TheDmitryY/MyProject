import uuid
from fastapi import APIRouter, Depends, status
from app.infrastructure.repositories.auth import get_password_service, get_token_service
from app.domain.entities.auth import LoginRequest, TokenResponse
from app.domain.entities.response import APIResponse
from app.domain.services.auth import PasswordService, TokenService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(
    request: LoginRequest,
    password_service: PasswordService = Depends(get_password_service),
    token_service: TokenService = Depends(get_token_service)
):
    if request.username == "admin" and request.password == "admin":
        user_id = uuid.uuid4()
        access_token = token_service.create_access_token(user_id)
        refresh_token = token_service.create_refresh_token(user_id)
        
        data = TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token
        )
        return APIResponse.success_response(data=data)
    
    return APIResponse.error_response(
        errors="Invalid credentials", 
        status_code=status.HTTP_401_UNAUTHORIZED
    )

@router.post("/refresh")
async def refresh_token(
    refresh_token: str,
    token_service: TokenService = Depends(get_token_service)
):
    user_id_str = token_service.verify_token(refresh_token)
    if not user_id_str:
        return APIResponse.error_response(
            errors="Invalid refresh token", 
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    
    user_id = uuid.UUID(user_id_str)
    access_token = token_service.create_access_token(user_id)
    new_refresh_token = token_service.create_refresh_token(user_id)
    
    data = TokenResponse(
        access_token=access_token,
        refresh_token=new_refresh_token
    )
    return APIResponse.success_response(data=data)
