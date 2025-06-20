from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,nullable=False,primary_key=True)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at =Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    votes = relationship("Vote", back_populates="user")
class Post(Base):# class name sould always be capital
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True, nullable=False)
    title = Column(String,nullable=False)
    content=Column(String,nullable=False)
    published =Column(Boolean,server_default='T',nullable=False)
    created_at =Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner = relationship("User")
    votes = relationship("Vote", back_populates="post")
    owner = relationship("User")




class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    post = relationship("Post", back_populates="votes")
    user = relationship("User", back_populates="votes")


