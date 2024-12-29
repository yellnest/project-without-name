from pydantic_settings import BaseSettings
from redis import Redis


class Settings(BaseSettings):
    #  DB info
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    #  Redis info
    REDIS_HOST: str

    #  JWT tokens info
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES:int

    #  Email info
    EMAIL_NAME: str
    EMAIL_PASS: str
    EMAIL_HOST: str
    EMAIL_PORT: int

    def get_db_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    def get_redis_url(self):
        return f"redis://{self.REDIS_HOST}:6379"

    def get_redis_connection(self):
        return Redis.from_url(self.get_redis_url())


    class Config:
        env_file = '.env'


settings = Settings()
