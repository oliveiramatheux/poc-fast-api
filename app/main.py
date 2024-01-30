import core.config  # type: ignore
import uvicorn

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal, engine, Base
from api.routers.health_check import router

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    # Lógica de consulta ao banco de dados usando a sessão db
    # Por exemplo: db.query(User).filter(User.id == item_id).first()
    pass


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
