import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    FIB_SEQ_MIN: int = 0
    FIB_SEQ_MAX: int = 1000
    DATABASE_URL = "mysql+aiomysql://root:123@mysql/test"


class LocalConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass


class StagingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


env = os.getenv("ENV", "local")


def get_config():
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "staging": StagingConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
