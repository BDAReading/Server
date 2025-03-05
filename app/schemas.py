from pydantic import BaseModel, EmailStr, Field, condecimal
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo


"""pydantic API 요청 데이터 검증 모델들"""


# Profile 생성
class ProfileCreate(BaseModel):
    bio: Optional[str] = None
    image: Optional[str] = None
    sns_link: Optional[str] = None
    location: Optional[str] = None
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(ZoneInfo("Asia/Seoul"))
    )


# User 생성
class UserCreate(BaseModel):
    nickname: str
    email: EmailStr
    password: str
    profile: ProfileCreate  # 회원가입 시 프로필도 생성


# Post 생성
class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int
    book_id: int
    rating: condecimal(max_digits=2, decimal_places=1)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(ZoneInfo("Asia/Seoul"))
    )


# Profile 응답
class ProfileResponse(BaseModel):
    bio: Optional[str] = None
    image: Optional[str] = None
    sns_link: Optional[str] = None
    location: Optional[str] = None


# User 응답
class UserResponse(BaseModel):
    nickname: str
    email: str
    profile: ProfileResponse


# Post 응답
class PostResponse(BaseModel):
    title: str
    content: str
    book_id: int
    rating: condecimal(max_digits=2, decimal_places=1)
    created_at: datetime
    nickname: str
