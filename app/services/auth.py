from fastapi import HTTPException


class AuthService:
    def login(self):
        raise HTTPException(status_code=403, detail="Forbidden area")
