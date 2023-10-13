from sqlalchemy import func, and_
from src.models import Student, Teacher, Discipline, Grade
from src.db import session


"""Середній бал, який певний викладач ставить певному студентові.

ORDER BY s.fullname  ; 
"""
def select_10(student_id, teacher_id): 
    result = session.query(Student.fullname, Teacher.fullname, func.avg(Grade.grade)) \
        .select_from(Grade)\
        .join(Student)\
        .where(Student.id == Grade.student_id)\
        .join(Discipline)\
        .where(and_(Discipline.id == Grade.discipline_id))\
        .join(Teacher)\
        .where(and_(Teacher.id==Discipline.teacher_id))\
        .filter(and_(Student.id == student_id, Teacher.id == teacher_id))\
        .all()
    return result


if __name__ == '__main__':
    print(select_10(53,8))
