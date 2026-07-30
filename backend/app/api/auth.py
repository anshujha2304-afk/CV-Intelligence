from fastapi import APIRouter

from app.schemas.auth import (
    SignUpRequest,
    LoginRequest,
    AuthResponse,
)

from app.services.auth_service import (
    sign_up,
    login,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/signup",
    response_model=AuthResponse,
    summary="Create a new account",
)
async def signup(user: SignUpRequest):

    response = sign_up(
        user.email,
        user.password,
    )

    session = response.session

    if session is None:
        return {
            "access_token": "",
            "refresh_token": "",
            "token_type": "bearer",
        }

    return {
        "access_token": session.access_token,
        "refresh_token": session.refresh_token,
        "token_type": "bearer",
    }


@router.post(
    "/login",
    response_model=AuthResponse,
    summary="Login",
)
async def login_user(user: LoginRequest):

    response = login(
        user.email,
        user.password,
    )

    session = response.session

    return {
        "access_token": session.access_token,
        "refresh_token": session.refresh_token,
        "token_type": "bearer",
    }