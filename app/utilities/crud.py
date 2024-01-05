# crud.py
from sqlalchemy.orm import Session
from pydantic import EmailStr
from app.models import Tradesman
import bcrypt
from sqlalchemy.future import select


async def get_trader_by_email(db: Session, email: EmailStr):
    # Construct an SQL expression
    stmt = select(Tradesman).filter(Tradesman.email == email)
    
    # Execute the query asynchronously
    result = await db.execute(stmt)
    
    # Fetch the first result
    check_exists = result.scalar_one_or_none()
    
    if not check_exists:
        return False
    else:
        return check_exists

async def get_trader_by_id(db: Session, id: str):
    stmt = select(Tradesman).filter(Tradesman.id == id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

# Utility functions for JWT and security
def verify_password(plain_password: str, hashed_password: str) -> bool:
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

async def authenticate_trader(db: Session, email: str, password: str):
    user = await get_trader_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def new_trader(db: Session, user):
    hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    hashed_password_str = hashed_password.decode('utf-8') 
    db_user = Tradesman(email=user.email, hashed_password=hashed_password_str)
    
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


