from app.domain.models import UserRegister
from app.domain.ports import UserRepositoryPort
from app.infrastructure.db.models import UserORM
from app.infrastructure.db.database import SessionLocal
from passlib.hash import bcrypt


class UserRepository(UserRepositoryPort):

    def create_user(self, user: UserRegister) -> dict:
        db = SessionLocal()
        try:
            hashed_password = bcrypt.hash(user.password)
            db_user = UserORM(
                name=user.name,
                email=user.email,
                hashed_password=hashed_password
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return {
                "id": db_user.id,
                "name": db_user.name,
                "email": db_user.email
            }
        finally:
            db.close()

    def authenticate_user(self, email: str, password: str) -> dict | None:
        db = SessionLocal()
        try:
            db_user = db.query(UserORM).filter(UserORM.email == email).first()
            if db_user and bcrypt.verify(password, db_user.hashed_password):
                return {
                    "id": db_user.id,
                    "name": db_user.name,
                    "email": db_user.email
                }
            return None
        finally:
            db.close()