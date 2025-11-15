from fastapi import HTTPException

from app.api.models.user import User
from app.api.schemas.user import UserCreate


class AuthService:
    async def signup(self, new_user: UserCreate) -> User:
        existing = await User.find_one(User.email == new_user.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already exists")

        user = User(**new_user.model_dump())
        await user.insert()
        return user
