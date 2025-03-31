from abc import ABC, abstractmethod
from .models import UserRegister

class UserRepositoryPort(ABC):

    @abstractmethod
    def create_user(self, user: UserRegister) -> dict:
        """Registra un nuevo usuario"""
        pass

    @abstractmethod
    def authenticate_user(self, email: str, password: str) -> dict | None:
        """Autentica un usuario y devuelve sus datos si son válidos"""
        pass