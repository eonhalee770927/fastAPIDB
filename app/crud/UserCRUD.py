from sqlalchemy.orm import Session

from app.models import UserModel
from app.schemas import UserSchema

def get_user(db: Session, user_id: int):
    return db.query(UserModel.User).filter(UserModel.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(UserModel.User).filter(UserModel.User.email == email).first()

def get_users(db: Session, skip:int=0, limit:int=100):
    # return db.query(models.User).offset(skip).limit(limit).all()
    return db.query(UserModel.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserSchema.UserCreate):
    db_user = UserModel.User(email=user.email,
                             name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_todos(db: Session, skip:int=0, limit: int=100):
    return db.query(UserModel.Todo).offset(skip).limit(limit).all()

def create_user_todo(db:Session, todo: UserSchema.TodoCreate, user_id : int):
    db_todo = UserModel.Todo(**todo.model_dump(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# NOTE :
# - add that instance object to your database session.
# - commit the changes to the database (so that they are saved).
# - refresh your instance (so that it contains any new data from the database, like the generated ID).