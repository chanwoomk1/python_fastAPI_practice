from pydantic import BaseModel

class StudyUpdate(BaseModel):
    student_id: int
    additional_hours: float



class StudentCreate(BaseModel):
    id: int
    user_age: int
    gender: str
    academic_level: str
    study_time: float