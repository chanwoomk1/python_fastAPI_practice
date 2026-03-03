from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import util.project_resource_path as project_resource_path

DATABASE_URL = f"sqlite:///{project_resource_path.project_path}/fastdb.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 여기서 딱 한 번만 Base를 만듭니다.
Base = declarative_base()