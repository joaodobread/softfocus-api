from pydantic import BaseModel, EmailStr, constr


class SignIn(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class AccessToken(BaseModel):
    token: str
