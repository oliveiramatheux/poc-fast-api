import core.config  # type: ignore
import uvicorn

from fastapi import FastAPI

from db.database import engine, Base
from api.routers.health_check import router
from api.routers.users import router_users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(router_users)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
