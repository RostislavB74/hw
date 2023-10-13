from sqlalchemy import func, and_
from src.models import Student, Teacher, Discipline, Grade
from src.db import session




"""Середній бал, який певний викладач ставить певному студентові.
SELECT students.fullname AS students_fullname, teachers.fullname AS teachers_fullname, ROUND(AVG(grades.grade), 2) AS avg_grade
FROM grades
JOIN students ON students.id = grades.student_id
JOIN disciplines ON disciplines.id = grades.discipline_id
JOIN teachers ON teachers.id = disciplines.teacher_id
WHERE students.id = grades.student_id AND disciplines.id = grades.discipline_id AND teachers.id = disciplines.teacher_id AND students.id = 53 AND disciplines.teacher_id =8
GROUP BY students.fullname, teachers.fullname
ORDER BY students.fullname;

"""
def select_11(student_id, teacher_id): 
    result = session.query(Student.fullname, Teacher.fullname, (func.round(func.avg(Grade.grade), 2))) \
        .select_from(Grade)\
        .join(Student).where(Student.id == Grade.student_id)\
        .join(Discipline).where(Discipline.id == Grade.discipline_id)\
        .join(Teacher).where(Teacher.id==Discipline.teacher_id)\
        .filter(and_(Student.id == student_id, Discipline.teacher_id == teacher_id))\
        .group_by(Student.fullname, Teacher.fullname)\
        .order_by(Student.fullname)\
        .all()
    return result

if __name__ == '__main__':
    print(select_11(53,10))
