from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings


if not find_dotenv():
    exit("Environment variables are not loaded because the file is missing .env")
else:
    load_dotenv()


class Settings(BaseSettings):
   secret_key: str

   class Config:
       env_file = ".env"


settings = Settings()
