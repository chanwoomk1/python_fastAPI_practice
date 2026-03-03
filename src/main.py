from db.db_setting import SessionLocal
from db.entity.student import Student

if __name__ == "__main__":
    db = SessionLocal()
    
    # 상위 5명 조회 테스트
    results = db.query(Student).limit(5).all()
    
    for s in results:
        print(f"ID: {s.id}, 나이: {s.user_age}, 공부시간: {s.study_time}")
        
    db.close()