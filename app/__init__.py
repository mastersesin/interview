from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi_pagination import add_pagination
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from core.config import config

engine = create_async_engine(config.DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
fast_app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@fast_app.on_event("startup")
async def startup():
    # TODO: We already implement pagination but still can improve it by next_page token
    import app.db.model.transaction
    # create db tables
    async with engine.begin() as conn:
        # Add pagination prevent edge case
        add_pagination(fast_app)
        await conn.run_sync(Base.metadata.create_all)
