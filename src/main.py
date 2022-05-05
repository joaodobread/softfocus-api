from fastapi import FastAPI


from .auth import auth_router
from .analysts import analysts_router
from .loss_communication import loss_communication_router

app = FastAPI(
    title='Softfocus API',
)

app.include_router(auth_router.router, tags=['auth'])
app.include_router(analysts_router.router, tags=['analysts'])
app.include_router(loss_communication_router.router,
                   tags=['loss communication'])
