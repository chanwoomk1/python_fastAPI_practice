
import util.project_resource_path as project_resource_path

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# DATABASE_URL = f"sqlite:///{project_resource_path.project_path}/fastdb.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db  
#     finally:
#         db.close() 
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

# sqlite 뒤에 +aiosqlite 추가
ASYNC_DB_URL = f"sqlite+aiosqlite:///{project_resource_path.project_path}/fastdb.db"

engine = create_async_engine(ASYNC_DB_URL)
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
