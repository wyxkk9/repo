from sqlalchemy.orm import Session
from app.db.models import Group, Student

# 创建组
def create_group(db: Session, name: str):
    group = Group(name=name)
    db.add(group)
    db.commit()
    db.refresh(group)
    return group

# 获取组
def get_group_by_id(db: Session, group_id: int):
    return db.query(Group).filter(Group.id == group_id).first()

# 删除组
def delete_group(db: Session, group_id: int):
    group = db.query(Group).filter(Group.id == group_id).first()
    if group:
        db.delete(group)
        db.commit()
    return group

# 获取所有组
def get_all_groups(db: Session):
    return db.query(Group).all()

# 将学生添加到组
def add_student_to_group(db: Session, student_id: int, group_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    group = db.query(Group).filter(Group.id == group_id).first()
    if student and group:
        group.students.append(student)
        db.commit()
        return group
    return None

# 将学生从组中移除
def remove_student_from_group(db: Session, student_id: int, group_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    group = db.query(Group).filter(Group.id == group_id).first()
    if student and group:
        group.students.remove(student)
        db.commit()
        return group
    return None

# 获取组中的所有学生
def get_students_in_group(db: Session, group_id: int):
    group = db.query(Group).filter(Group.id == group_id).first()
    return group.students if group else None

# 将学生从组 A 移动到组 B
def move_student_between_groups(db: Session, student_id: int, from_group_id: int, to_group_id: int):
    remove_student_from_group(db, student_id, from_group_id)
    add_student_to_group(db, student_id, to_group_id)