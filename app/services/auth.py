from app.api.models.user import User
from app.api.schemas.user import UserCreate
from app.configs.exceptions.api_error import ApiError
from app.configs.exceptions.decorators import trycatch


class AuthService:
    @trycatch
    async def signup(self, new_user: UserCreate) -> User:
        username = new_user.username.strip()
        email = new_user.email.strip()
        password = new_user.password.strip()

        if not username:
            raise ApiError(400, "Username is required")
        if not email:
            raise ApiError(400, "Email is required")
        if not password:
            raise ApiError(400, "Password is required")

        existing = await User.find_one(User.email == new_user.email)
        if existing:
            raise ApiError(400, "Email already exists.")

        user = User(**new_user.model_dump())
        await user.insert()
        return user
