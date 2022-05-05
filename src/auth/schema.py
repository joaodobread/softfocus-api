from pydantic import BaseModel


class SignIn(BaseModel):
    email: str
    password: str


class AccessToken(BaseModel):
    access_token: str
