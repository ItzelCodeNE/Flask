from models import Base,User,Comment
from Connection import engine


Base.metadata.create_all(bind=engine)
