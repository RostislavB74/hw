from sqlalchemy import func, and_
from src.models import Student, Teacher, Discipline, Grade
from src.db import session




"""Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT teachers.fullname AS teachers_fullname, ROUND(AVG(grades.grade), 2) AS avg_grade
FROM grades
JOIN disciplines ON disciplines.id = grades.discipline_id
JOIN teachers ON teachers.id = disciplines.teacher_id
WHERE teachers.id = disciplines.teacher_id AND disciplines.teacher_id =8
GROUP BY teachers.fullname
ORDER BY teachers.fullname;

"""
def select_8(teacher_id): 
    result = session.query(Teacher.fullname, (func.round(func.avg(Grade.grade), 2))) \
        .select_from(Grade)\
        .join(Discipline).where(Discipline.id == Grade.discipline_id)\
        .join(Teacher).where(Teacher.id==Discipline.teacher_id)\
        .filter(Discipline.teacher_id == teacher_id)\
        .group_by(Teacher.fullname)\
        .order_by(Teacher.fullname)\
        .all()
    return result

if __name__ == '__main__':
    print(select_8(10))
