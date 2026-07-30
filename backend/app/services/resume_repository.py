from fastapi import HTTPException
from postgrest.exceptions import APIError

from app.core.database import supabase

TABLE = "resumes"


def save_resume(user_id: str, data: dict):
    data["user_id"] = user_id

    try:
        response = (
            supabase.table(TABLE)
            .insert(data)
            .execute()
        )

        if response.data:
            return response.data[0]

        return None

    except APIError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {e.message}",
        )


def get_latest_resume(user_id: str):
    try:
        response = (
            supabase.table(TABLE)
            .select("*")
            .eq("user_id", user_id)
            .order("created_at", desc=True)
            .limit(1)
            .execute()
        )

        if response.data:
            return response.data[0]

        return None

    except APIError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {e.message}",
        )


def get_resume_by_id(user_id: str, resume_id: str):
    try:
        response = (
            supabase.table(TABLE)
            .select("*")
            .eq("id", resume_id)
            .eq("user_id", user_id)
            .execute()
        )

        if response.data:
            return response.data[0]

        return None

    except APIError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {e.message}",
        )


def list_resumes(user_id: str):
    try:
        response = (
            supabase.table(TABLE)
            .select("id, filename, name, email, ats_score, created_at")
            .eq("user_id", user_id)
            .order("created_at", desc=True)
            .execute()
        )

        return response.data

    except APIError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {e.message}",
        )


def delete_resume(user_id: str, resume_id: str):
    try:
        response = (
            supabase.table(TABLE)
            .delete()
            .eq("id", resume_id)
            .eq("user_id", user_id)
            .execute()
        )

        return response.data

    except APIError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {e.message}",
        )