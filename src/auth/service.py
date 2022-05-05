from time import time
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.analysts.service import AnalystsService, make_analyst_service
from src.common.bcrypt import BcryptAdapter
from src.common.jwt_generator import JwtHandler


def make_auth_service(db: Session):
    return AuthService(make_analyst_service(db), BcryptAdapter())


class AuthService:
    def __init__(self, repository: AnalystsService, bcrypt: BcryptAdapter) -> None:
        self.repository = repository
        self.bcrypt = bcrypt

    def sign_in(self, email: str, password: str) -> str:
        analyst = self.repository.find_by_email(email)
        if not self.bcrypt.compare_hash(password, analyst.password):
            raise HTTPException(401, "invalid_access_credentials")
        token = JwtHandler.sign(
            sub=str(analyst.id),
            email=analyst.email,
            iat=int(time())
        )
        return token
