from sqlalchemy import func, desc, select, and_

from src.models import Group, Grade, Student, Discipline
from src.db import session


def select_one(discipline_id):
    """
   Знайти середній бал у групах з певного предмета.
SELECT i.name0, gr.name, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN items i ON i.id = g.items_id
JOIN [groups] gr ON gr.id =s.group_id 
WHERE i.id = 5
GROUP  BY gr.name, i.name
ORDER BY average_grade DESC 
subq = (
    select(func.count(addresses.c.id))
    .where(users.c.id == addresses.c.user_id)
    .scalar_subquery()
)
    """
    result = session.query(Discipline.name, Group.name, func.round(func.avg(Grade.grade), 2)) \
        .select_from(Grade)\
        .join(Student)\
        .where(Student.id == Grade.student_id)\
        .join(Discipline)\
        .where(Discipline.id == Grade.discipline_id)\
        .join(Group)\
        .where(Group.id == Student.group_id)\
        .filter(Discipline.id == discipline_id)\
        .group_by(Group.name, Discipline.name)\
        .all()
    return result


if __name__ == '__main__':
    print(select_one(1))
