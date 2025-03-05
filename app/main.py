from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated
import models
import schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session, joinedload

app = FastAPI()
# ORM에서 정의한 테이블을 실제 DB에 생성
models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()  # 세션 객체 생성
    try:
        yield db  # 세션 객체 반환
    finally:
        db.close()  # 요청이 끝나면 세션 종료


db_dependency = Annotated[Session, Depends(get_db)]


# 회원가입
@app.post("/sign-up", status_code=status.HTTP_201_CREATED)
async def sign_up(user: schemas.UserCreate, db: db_dependency):
    try:
        # 유저 생성
        db_user = models.User(**user.model_dump(exclude={"profile"}))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        # 프로필 생성
        db_profile = models.Profile(
            user_id=db_user.user_id, **user.profile.model_dump()
        )
        db.add(db_profile)
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error: {str(e)}")


# 게시글 작성
@app.post("/post-create/", status_code=status.HTTP_201_CREATED)
async def create_post(post: schemas.PostCreate, db: db_dependency):
    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()


# 프로필 확인
@app.get(
    "/users/{user_id}",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_200_OK,
)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# 게시글 확인
@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id: int, db: db_dependency):
    post = (
        db.query(models.Post)
        .options(joinedload(models.Post.user))
        .filter(models.Post.id == post_id)
        .first()
    )
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


# @app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
# async def delete_post(post_id: int, db: db_dependency):
#     db_post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     db.delete(db_post)
#     db.commit()
