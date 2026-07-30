from fastapi import HTTPException

from app.core.database import supabase


def sign_up(email: str, password: str):
    response = supabase.auth.sign_up(
        {
            "email": email,
            "password": password,
        }
    )

    if response.user is None:
        raise HTTPException(
            status_code=400,
            detail="Unable to create account.",
        )

    return response


def login(email: str, password: str):
    response = supabase.auth.sign_in_with_password(
        {
            "email": email,
            "password": password,
        }
    )

    if response.user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password.",
        )

    return response


def logout(jwt: str):
    supabase.auth.sign_out(jwt)