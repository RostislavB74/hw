from sqlalchemy import func, and_
from src.models import Student, Teacher, Discipline, Grade
from src.db import session




"""Середній бал, який певний викладач ставить певному студентові.
ELECT s.fullname AS 'Студент',  i.name as 'Предмет', t.fullname as 'Викладач', ROUND (AVG(g.grade),2) AS 'Середній бал'
FROM grades g  
JOIN students s ON s.id=g.student_id
JOIN teachers t ON t.id=g.items_id
JOIN items i ON i.id = g.items_id 
WHERE s.id = 11 AND i.id =5
--IF WHERE i.id =1
GROUP BY i.id 


ORDER BY s.fullname  ; 
"""
def select_11(student_id, teacher_id): 
    result = session.query(Student.fullname, Teacher.fullname, func.round(func.avg(Grade.grade), 2)) \
        .select_from(Grade)\
        .join(Student)\
        .where(Student.id == Grade.student_id)\
        .join(Discipline)\
        .where(and_(Discipline.id == Grade.discipline_id))\
        .join(Teacher)\
        .where(and_(Teacher.id==Discipline.teacher_id))\
        .all()
        # .filter(and_(Student.id == student_id, Teacher.id == teacher_id))\
        
    return result


if __name__ == '__main__':
    print(select_11(53,10))
