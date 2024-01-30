from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
