from fastapi import APIRouter, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import AccountAPI
import jwt
from app import config
import datetime

user_route = APIRouter()


# @user_route.post("/auth/magic-link")
# async def magic_link(email: str, background_tasks: BackgroundTasks):

#     if AccountAPI().get_user_email(email):
#         # Generate a secure token
#         token = jwt.encode({"email": email, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15)}, config.SECRET_KEY, algorithm=config.ALGORITHM)

#         # add logic to get the company url
#         # Create a magic link containing the token
#         link = f"http://yourfrontenddomain.com/authenticate?token={token}"
        
#         # Send the email in the background
#         background_tasks.add_task(send_email, email, link)
        
#         return {"message": "Magic link sent to your email!"}

# @user_route.get("/auth/validate-magic-link")
# async def validate_magic_link(token: str):
#     try:
#         # Decode and validate token
#         payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
#         email = payload.get("email")
        
#         # Here, implement logic to find the user by email and create a user session or a new token
        
#         return {"message": f"Welcome {email}!"}
#     except jwt.JWTError:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")
