from app.domain.models import UserRegister
from app.domain.ports import UserRepositoryPort
from app.infrastructure.auth.jwt_handler import create_token


class UserService:
    def __init__(self, repository: UserRepositoryPort):
        self.repo = repository

    def register(self, user: UserRegister) -> dict:
        return self.repo.create_user(user)

    def login(self, email: str, password: str) -> dict | None:
        user_data = self.repo.authenticate_user(email, password)
        if user_data:
            token = create_token(email)
            return {
                "id": user_data["id"],
                "name": user_data["name"],
                "email": user_data["email"],
                "access_token": token
            }
        return None