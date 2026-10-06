from fastapi import APIRouter, HTTPException

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user


router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate):
    return create_user(user)


@router.get("/{user_identification}", response_model=UserResponse)
def get_existing_user(user_identification: int):
    user = get_user(user_identification)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user
