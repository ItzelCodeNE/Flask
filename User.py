from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR 
from sqlalchemy.orm import sessionmaker,declarative_base

Base = declarative_base()


class user(Base):
    __tablename__ = 'User'

    id = Column('ID', Integer, primary_key = True)
    Username = Column('Username',String(10),nullable = False)
    email = Column('Email',String(15),nullable = False)
    password = Column('Password',String(30),nullable = False)


    def __init__(self,id,Username,email,password):
        self.id = id
        self.Username = Username
        self.email = email
        self.password = password


    def __repr__(self): 
        return f'({self.id} , {self.Username} , {self.email})'
    

engine = create_engine('sqlite:///IRSv2b3.db', echo= True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

User1 = user(0,'ItzelCNE','Itzel.cne@gmail.com','Testpassword')
session.add(User1)
session.commit()
