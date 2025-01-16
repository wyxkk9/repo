from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import student_service, group_service

router = APIRouter()

# 创建学生
@router.post("/students/")
def create_student(name: str, age: int, db: Session = Depends(get_db)):
    return student_service.create_student(db, name, age)

# 获取学生信息
@router.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = student_service.get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# 获取学生列表
@router.get("/students/")
def list_students(db: Session = Depends(get_db)):
    return student_service.get_all_students(db)

# 删除学生
@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = student_service.delete_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": f"Student with ID {student_id} deleted"}

# 创建组
@router.post("/groups/")
def create_group(name: str, db: Session = Depends(get_db)):
    return group_service.create_group(db, name)

# 获取组信息
@router.get("/groups/{group_id}")
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = group_service.get_group_by_id(db, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group

# 获取组列表
@router.get("/groups/")
def list_groups(db: Session = Depends(get_db)):
    return group_service.get_all_groups(db)

# 删除组
@router.delete("/groups/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db)):
    group = group_service.delete_group(db, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"detail": f"Group with ID {group_id} deleted"}

# 将学生添加到组
@router.post("/groups/{group_id}/students/{student_id}")
def add_student_to_group(group_id: int, student_id: int, db: Session = Depends(get_db)):
    group = group_service.add_student_to_group(db, student_id, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group or student not found")
    return {"detail": f"Student {student_id} added to group {group_id}"}

# 将学生从组中移除
@router.delete("/groups/{group_id}/students/{student_id}")
def remove_student_from_group(group_id: int, student_id: int, db: Session = Depends(get_db)):
    group = group_service.remove_student_from_group(db, student_id, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group or student not found")
    return {"detail": f"Student {student_id} removed from group {group_id}"}

# 获取组中的所有学生
@router.get("/groups/{group_id}/students/")
def get_students_in_group(group_id: int, db: Session = Depends(get_db)):
    students = group_service.get_students_in_group(db, group_id)
    if students is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return students

# 将学生从组 A 移动到组 B
@router.put("/groups/{from_group_id}/students/{student_id}/to/{to_group_id}")
def move_student_between_groups(from_group_id: int, to_group_id: int, student_id: int, db: Session = Depends(get_db)):
    group_service.move_student_between_groups(db, student_id, from_group_id, to_group_id)
    return {"detail": f"Student {student_id} moved from group {from_group_id} to group {to_group_id}"}