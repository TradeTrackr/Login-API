from pydantic import BaseModel, EmailStr, UUID4


class TraderRegistration(BaseModel):
    email: EmailStr
    password: str

class TradesmanResponse(BaseModel):
    id: UUID4
    email: EmailStr

class RefreshToken(BaseModel):
    refresh_token: str
