import uuid

from fastapi import Header, HTTPException
from jose import jwt

from config import SECRET_KEY


async def verify_token(authorization: str = Header("Authorization")):
    """Verify JWT token for protected routes"""
    try:
        decoded_token = jwt.decode(
            authorization, str(SECRET_KEY), algorithms=["HS256"])
        if "code" in decoded_token:
            decoded_token['code'] = uuid.UUID(decoded_token['code'])
        return decoded_token
    except Exception as e:
        raise HTTPException(
            status_code=401, detail=f"[Authorization] {e}")
