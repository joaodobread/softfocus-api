> poetry run alembic upgrade heads

> poetry run alembic revision -m "loss_communication"

> uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

> poetry run alembic downgrade -1

ADDING A MIDDLEWARE
```python
def verify_token(authorization: str = Header(...)):
    print(authorization)
    return authorization


@router.post("/sign-in", response_model=schema.AccessToken, dependencies=[Depends(verify_token)])
```

$2b$12$gAe9jQmg8ID5OnzwZuxA7.bPhBbNe6KFCOkuLEDqitWw842kFDGKC -> 123

