class JwtDecoded:
    sub: str
    email: str

    def __init__(self, sub: str, email: str) -> None:
        self.sub = sub
        self.email = email
