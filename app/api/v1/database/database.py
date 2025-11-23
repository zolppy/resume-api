from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///app/api/v1/database.db"

engine = create_async_engine(url=DATABASE_URL)
base = declarative_base()
Session = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


async def create_tables():
    """
    Create tables in the database using SQLAlchemy's declarative_base.
    """
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)


async def get_db():
    """
    Async context manager that yields a database session.
    """
    db = Session()
    try:
        yield db
        await db.commit()
    except Exception:
        await db.rollback()
        raise
    finally:
        await db.close()
