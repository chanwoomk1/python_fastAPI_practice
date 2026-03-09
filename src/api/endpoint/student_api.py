from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


from core_DI.db_setting import get_db
from api.schemas.student_dto import  StudentCreate,StudyUpdate
from service import student_service
from models.student import Student

router = APIRouter(
    prefix="/students",
    tags=["students"]
)
# 3. 학습 통계 업데이트 
@router.put("/update-study")
async def update_study_stats(data: StudyUpdate, db: Session = Depends(get_db)):
    updated_student = await student_service.update_student_study_time(
        db, data.student_id, data.additional_hours
    )
    
    if not updated_student:
        raise HTTPException(status_code=404, detail="학생을 찾을 수 없습니다.")
        
    return {
        "message": "업데이트 성공",
        "student_id": updated_student.id,
        "new_study_time": updated_student.study_time,
        "new_academic_level": updated_student.academic_level
    }
# 1. 데이터 생성 (CREATE) - 비동기로 전환
@router.post("/create")
async def create_student(student_data: StudentCreate, db: AsyncSession = Depends(get_db)):
    # db.query 대신 비동기 방식 execute 사용
    result = await db.execute(select(Student).filter(Student.id == student_data.id))
    db_student = result.scalars().first()
    
    if db_student:
        raise HTTPException(status_code=400, detail="이미 존재하는 ID입니다.")
    
    new_student = Student(**student_data.model_dump()) # Pydantic v2 방식 (dict() 대신)
    
    db.add(new_student)
    await db.commit() # await 필수
    await db.refresh(new_student) # await 필수
    return new_student

# 2. 데이터 조회 (READ) - 비동기로 전환
@router.get("/find_by_id/{student_id}")
async def read_student(student_id: int, db: AsyncSession = Depends(get_db)): 
    result = await db.execute(select(Student).filter(Student.id == student_id))
    student = result.scalars().first()
    
    if student is None:
        raise HTTPException(status_code=404, detail="해당 학생을 찾을 수 없습니다.")
    return student