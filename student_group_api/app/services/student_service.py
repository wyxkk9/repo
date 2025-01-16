from sqlalchemy.orm import Session
from app.db.models import Student, Group

# 创建学生
def create_student(db: Session, name: str, age: int):
    student = Student(name=name, age=age)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

# 获取学生
def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

# 删除学生
def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student

# 获取所有学生
def get_all_students(db: Session):
    return db.query(Student).all()