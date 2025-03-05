from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text,
    DECIMAL,
)
from sqlalchemy.orm import relationship
from database import Base


# users 테이블
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    nickname = Column(String(10), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    pre_password = Column(String(255), nullable=True, server_default=None)

    profile = relationship(
        "Profile", back_populates="user", uselist=False, cascade="all, delete-orphan"
    )
    post = relationship("Post", back_populates="user", cascade="all, delete-orphan")


# profiles 테이블
class Profile(Base):
    __tablename__ = "profiles"

    user_id = Column(
        Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True
    )
    bio = Column(String(255), nullable=True, server_default=None)
    image = Column(String(255), nullable=True, server_default=None)
    sns_link = Column(String(255), nullable=True, server_default=None)
    location = Column(String(255), nullable=True, server_default=None)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True, server_default=None)

    user = relationship("User", back_populates="profile")


# books 테이블
class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author = Column(String(100))
    published_at = Column(DateTime, nullable=True, server_default=None)
    book_image = Column(String(255), nullable=True, server_default=None)
    isbn = Column(String(20), nullable=True, server_default=None)
    publisher = Column(String(100))
    description = Column(Text, nullable=True, server_default=None)

    post = relationship("Post", back_populates="book")


# posts 테이블
class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    book_id = Column(Integer, ForeignKey("books.book_id", ondelete="CASCADE"))
    title = Column(String(255))
    content = Column(Text)
    rating = Column(DECIMAL(2, 1))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user = relationship("User", back_populates="post")
    book = relationship("Book", back_populates="post")
