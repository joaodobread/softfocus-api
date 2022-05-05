from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.service import make_auth_service
from src.sqlalchemy.database import get_db
from . import schema

router = APIRouter(prefix="/auth")


@router.post("/sign-in", response_model=schema.AccessToken)
def sign_in(payload: schema.SignIn, db: Session = Depends(get_db)):
    service = make_auth_service(db)
    token = service.sign_in(payload.email, payload.password)

    return {
        "access_token": token
    }
