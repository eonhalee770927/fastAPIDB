from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import UserCRUD
from app.models import UserModel
from app.schemas import UserSchema
from app.db.database import SessionLocal, engine

UserModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=UserSchema.User)
def post_user(user: UserSchema.UserCreate, db:Session=Depends(get_db)):
    db_user = UserCRUD.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return UserCRUD.create_user(db=db, user=user)

@app.get("/users/", response_model=list[UserSchema.User])
def get_users(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    users = UserCRUD.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}/", response_model=UserSchema.User)
def get_user(user_id:int, db:Session=Depends(get_db)):
    db_user = UserCRUD.get_user(db, user_id =user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/todos/", response_model=UserSchema.Todo)
def post_todo_for_user(user_id:int, todo: UserSchema.TodoCreate, db:Session=Depends(get_db)):
    return UserCRUD.create_user_todo(db=db, user_id=user_id, todo=todo)

@app.get("/todos/", response_model=list[UserSchema.Todo])
def get_todos(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    todos = UserCRUD.get_todos(db, skip=skip, limit=limit)
    return todos