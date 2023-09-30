from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import ForeignKey,text



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'Users'
    id:Mapped[int] = mapped_column(primary_key=True)
    Username:Mapped[str] = mapped_column(nullable=False)
    Password:Mapped[int] = mapped_column(nullable=False)
    email:Mapped[str]

class Comment(Base):
    __tablename__ = 'Comments'
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey(User.id))
    text:Mapped[str] = mapped_column(text,nullable=False)


