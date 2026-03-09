from sqlalchemy.orm import Session
from models.student import Student
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

def calculate_academic_level(current_hours: float) -> str:
    if current_hours >= 10.0:
        return "Postgraduate"
    elif current_hours >= 5.0:
        return "Undergraduate"
    else:
        return "High School"


async def update_student_study_time(db: AsyncSession, student_id: int, additional_hours: float):
    # 1. 학생 조회
    result = await db.execute(select(Student).filter(Student.id == student_id))
    db_student = result.scalars().first()
    if not db_student:
        return None

    # 2. 공부 시간 증가
    db_student.study_time += additional_hours
    
    # 3. 변경된 시간에 따라 레벨 재계산
    new_level = calculate_academic_level(db_student.study_time)
    db_student.academic_level = new_level
    
    # 4. DB 반영
    await db.commit()
    await db.refresh(db_student)
    
    return db_student