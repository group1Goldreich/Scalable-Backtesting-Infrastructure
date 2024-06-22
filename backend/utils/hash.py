from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_value(password: str) -> str:
    return password_context.hash(password)


def compare_hash_value(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)