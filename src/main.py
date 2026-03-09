from contextlib import asynccontextmanager
from fastapi import FastAPI
from core_DI.db_setting import engine
from core_DI.base import Base
import models  
from api.endpoint.student_api import router as student_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    #실행권 반납
    yield
    # 실행권 회수 후 실행(program 종료)
    await engine.dispose()


app = FastAPI(title="비동기 학생 관리 서비스", lifespan = lifespan )
app.include_router(student_router)