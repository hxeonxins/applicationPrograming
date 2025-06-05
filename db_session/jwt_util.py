import secrets

from jose import jwt
from scipy._lib.cobyqa import settings

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"
SECRET_KEY = secrets.token_urlsafe(64)

def create_access_token(data: dict):
    to_encode = data.copy()
    import datetime
    expire = datetime.datetime.now() + datetime.timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
