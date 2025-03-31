from fastapi import APIRouter, HTTPException
from app.infrastructure.db.repository import UserRepository
from app.application.services import UserService
from app.domain.models import UserLogin, UserRegister, UserOut

router = APIRouter()
service = UserService(UserRepository())

@router.post("/register", response_model=UserOut)
def register(user: UserRegister):
    return service.register(user)

@router.post("/login")
def login(user: UserLogin):
    result = service.login(user.email, user.password)
    if not result:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return result
