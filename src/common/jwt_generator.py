import jwt
from decouple import config


class JwtGenerator:
    def sign(**kwargs):
        return jwt.encode(kwargs, key=config('SECRET_KEY'))
