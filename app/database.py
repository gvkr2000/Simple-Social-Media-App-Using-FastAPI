from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
from urllib.parse import quote_plus


username = quote_plus(settings.database_username)
password = quote_plus(settings.database_password)

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{username}:{password}@{settings.database_hostname}:{str(settings.database_port)}/{settings.database_name}"
)


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:

#     try:
       
#         conn = psycopg.connect( host="localhost",port=5432,dbname="Fast_API",user="postgres", password="Vamshi@123456")

#         cursor=conn.cursor()
#         print("Database connection was  succesfull :-)")
#         break
#     except Exception as error:
#         print("Connecting to database failed!!!")
#         print("error was",error)
#         time.sleep(60)