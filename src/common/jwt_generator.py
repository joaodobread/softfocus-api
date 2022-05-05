import jwt
from decouple import config


class JwtHandler:
    def sign(**kwargs):
        return jwt.encode(kwargs, key=config('SECRET_KEY'), algorithm="HS256")

    def verify(access_token: str):
        try:
            jwt.decode(access_token, key=config(
                'SECRET_KEY'), algorithms=["HS256"])
            return True
        except Exception as e:
            return False
