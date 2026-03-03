from sqlalchemy import Column, Integer, String, Float
from db.db_setting import Base

class Student(Base):
    __tablename__ = "student_stats" # 실제 DB 테이블 이름

    # id는 파이썬에서 쓸 이름, "student_id"는 실제 DB에 있는 컬럼 이름
    id = Column("student_id", String, primary_key=True)
    
    # 파이썬에선 user_age, DB에선 age
    user_age = Column("age", Integer)
    
    # DB 이름과 파이썬 변수명이 같으면 생략 가능
    gender = Column(String) 
    
    academic_level = Column("academic_level", String)
    study_time = Column("study_hours", Float) # DB는 study_hours, 파이썬은 study_time