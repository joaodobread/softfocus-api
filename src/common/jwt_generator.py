import jwt
from decouple import config

from src.common.jwt_decode import JwtDecoded


class JwtHandler:
    def sign(**kwargs):
        return jwt.encode(kwargs, key=config('SECRET_KEY'), algorithm='HS256')

    def verify(access_token: str):
        try:
            jwt.decode(access_token, key=config(
                'SECRET_KEY'), algorithms=['HS256'])
            return True
        except Exception as e:
            return False

    def decode(access_token: str):
        jwt_decoded = jwt.decode(access_token, key=config(
            'SECRET_KEY'), algorithms=['HS256'])

        return JwtDecoded(jwt_decoded['sub'], jwt_decoded['email'])
