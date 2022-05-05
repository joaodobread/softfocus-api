from typing import Optional
from fastapi import HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.common.jwt_generator import JwtHandler


class RequiredAuth(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        auth = await super().__call__(request)
        if not auth.credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authenticated'
            )
        if not JwtHandler.verify(auth.credentials):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authenticated'
            )
        return JwtHandler.decode(auth.credentials)
