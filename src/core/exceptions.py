from fastapi import status

class BaseAppException(Exception):
    """모든 비즈니스 예외의 부모 클래스"""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

class StudentNotFoundException(BaseAppException):
    """학생을 찾을 수 없을 때 발생하는 예외"""
    def __init__(self, student_id: int):
        super().__init__(
            message=f"ID가 {student_id}인 학생을 찾을 수 없습니다.", 
            status_code=404
        )


