from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.models.users import User

router_users = APIRouter()


@router_users.post("/users")
async def create_user(request: Request, db: Session = Depends(get_db)):
    body = await request.json()

    db_user = User(email=body.get('email'), password=body.get('password'))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
