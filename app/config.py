from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port : str = "5432"
    database_password : str = "password"
    database_name: str = "mydb"
    database_username: str = "user"
    secret_key: str = "supersecretkey"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"  

from dotenv import load_dotenv
load_dotenv()  # This loads the .env file into os.environ

settings = Settings() 
