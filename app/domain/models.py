from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRegister(UserLogin):
    name: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
