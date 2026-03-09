from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from core_DI.base import Base # 경로에 맞춰 수정

class Student(Base):
    __tablename__ = "student_stats"
    # --------- dbname = fastdb.db     tablename = student_stats ------------
    #   student_id,age,gender,academic_level,study_hours,self_study_hours,
    #   online_classes_hours,social_media_hours,gaming_hours,sleep_hours,
    #   screen_time_hours,exercise_minutes,caffeine_intake_mg,part_time_job,
    #   upcoming_deadline,internet_quality,mental_health_score,
    #   focus_index,burnout_level,productivity_score,exam_score


    # mapped_column을 사용하면 타입 힌트와 DB 설정을 동시에 할 수 있습니다.
    id: Mapped[int] = mapped_column("student_id", Integer, primary_key=True)
    user_age: Mapped[int] = mapped_column("age", Integer)
    gender: Mapped[str] = mapped_column(String)
    academic_level: Mapped[str] = mapped_column(String)
    study_time: Mapped[float] = mapped_column("study_hours", Float)