from fastapi import FastAPI
from .routers.trader import trader_route
from .routers.user import  user_route

app = FastAPI()

app.include_router(trader_route, prefix="/trader")
app.include_router(user_route, prefix="/user")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")