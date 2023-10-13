from sqlalchemy import func, and_
from src.models import Student, Group, Discipline, Grade
from src.db import session

"""--Знайти оцінки студентів у окремій групі з певного предмета.
SELECT gr.name as 'Група', s.fullname  as 'Студент', i.name as 'Предмет', g.grade as 'Оцінка', g.date_of 'Дата'
FROM grades g , [groups] gr, items i 
JOIN students s ON s.id  = g.items_id  -- ON i.id = g.items_id
WHERE gr.id  = 3 AND i.id=1 --AND s.id = 2
ORDER BY s.fullname  
"""


def select_7(group_id, items_id):
    result = session.query(Group.name, Student.fullname, Discipline.name, Grade.grade) \
        .select_from(Grade)\
        .join(Student)\
        .where(Student.id == Grade.student_id)\
        .join(Discipline)\
        .where(Discipline.id == Grade.discipline_id)\
        .join(Group)\
        .where(Group.id == Student.group_id)\
        .filter(and_(Discipline.id == items_id, Group.id == group_id))\
        .all()
    return result


if __name__ == '__main__':
    print(select_7(2, 3))
