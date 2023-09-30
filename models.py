from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,text
from typing import List



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'Users'
    id:Mapped[int] = mapped_column(primary_key=True)
    Username:Mapped[str] = mapped_column(nullable=False)
    Password:Mapped[int] = mapped_column(nullable=False)
    email:Mapped[str]
    comment:Mapped[List["Comment"]] = relationship(back_populates='user')


class Comment(Base):
    __tablename__ = 'Comments'
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey(User.id))
    text:Mapped[str] = mapped_column(text,nullable=False)
    user:Mapped["User"] =relationship(back_populates=false)


