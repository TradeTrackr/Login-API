from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.utilities.db import get_db
from app.utilities.crud import get_trader_by_id, authenticate_trader, get_trader_by_email, new_trader
from fastapi.security import OAuth2PasswordRequestForm
from app.utilities.authentication import Authentication
from app.validation_models import TraderRegistration, RefreshToken


trader_route = APIRouter()
TraderRegistration
# trader register
@trader_route.post("/register")
async def register(user: TraderRegistration, db: AsyncSession = Depends(get_db)) -> dict:
    
    existing_trader = await get_trader_by_email(db, user.email)

    if existing_trader:
        raise HTTPException(status_code=400, detail="Email already registered")

    trader_user = await new_trader(db, user)

    return {"message": "User created successfully.", "id": trader_user.id}

# trader login
@trader_route.post("/login", status_code=200)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    trader = await authenticate_trader(db, form_data.username, form_data.password)
    if not trader:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = Authentication.create_access_token(data={"sub": str(trader.id)})
    refresh_token = Authentication.create_refresh_token(data={"sub": str(trader.id)})
    return {
        "id": str(trader.id),
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

# # trader token refresh
# @trader_route.post("/token/refresh", status_code=200)
# async def token_refresh(data: RefreshToken, db: AsyncSession = Depends(get_db)) -> dict:

#     id = Authentication.validate_refresh_token(data.refresh_token)

#     trader = await get_trader_by_id(db, id)
#     if trader is None:
#         raise HTTPException(status_code=404, detail="Trader not found")

#     access_token = Authentication.create_access_token(data={"sub": str(trader.id)})
#     refresh_token = Authentication.create_refresh_token(data={"sub": str(trader.id)})
#     return {
#         "access_token": access_token,
#         "refresh_token": refresh_token,
#         "token_type": "bearer"
#     }

# # trader token validate
# @trader_route.post("/token/validate", status_code=200)
# async def token_validate(token: str, db: AsyncSession = Depends(get_db)) -> dict:

#     id = Authentication.validate_token(token)

#     trader = await get_trader_by_id(db, id)
#     if trader is None:
#         raise HTTPException(status_code=404, detail="Trader not found")

#     access_token = Authentication.create_access_token(data={"sub": str(trader.id)})
#     refresh_token = Authentication.create_refresh_token(data={"sub": str(trader.id)})
#     return {
#         "access_token": access_token,
#         "refresh_token": refresh_token,
#         "token_type": "bearer"
#     }


# trader logout
@trader_route.post("/logout", status_code=200)
async def logout(db: AsyncSession = Depends(get_db)) -> dict:
    trader = await get_trader_by_id(db, id)
    if trader is None:
        raise HTTPException(status_code=404, detail="Trader not found")
    return {"trader": trader}


@trader_route.get("/")
async def health():

    return 'hi'
