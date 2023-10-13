from sqlalchemy import func, and_
from src.models import Student, Group, Discipline, Grade
from src.db import session


"""Знайти список курсів, які відвідує певний студент.
SELECT s.fullname AS 'Студент',  i.name as 'Предмет'
FROM grades g  
JOIN students s ON s.id=g.student_id
JOIN items i ON i.id = g.items_id 
WHERE s.id = 11
--WHERE i.id =1
GROUP BY i.id 


ORDER BY s.fullname  ; 
"""
def select_9(student_id): 
    result = session.query(Student.fullname, Discipline.name) \
        .select_from(Grade)\
        .join(Student)\
        .where(Student.id == Grade.student_id)\
        .join(Discipline)\
        .where(Discipline.id == Grade.discipline_id)\
        .filter(Student.id == student_id)\
        .group_by(Student.fullname, Discipline.name)\
        .all()
    return result


if __name__ == '__main__':
    print(select_9(2))
