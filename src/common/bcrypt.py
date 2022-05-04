import bcrypt


class BcryptAdapter:
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(
            password=password.encode('utf-8'), salt=salt)
        return hashed_password.decode('utf-8')

    def compare_hash(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'),
                              hashed_password.encode('utf-8'))
