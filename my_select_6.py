from src.models import Student, Group
from src.db import session

"""Знайти список студентів у певній групі.
SELECT s.fullname  as 'Студент', g.name as 'Група'
FROM [groups] g
JOIN students s ON s.group_id  = g.id  
WHERE g.id  = 3
ORDER BY s.fullname  
"""


def select_6(group_id):
    result = session.query(Student.fullname, Group.name) \
        .select_from(Group)\
        .join(Student)\
        .where(Student.group_id == Group.id)\
        .filter(Group.id == group_id)\
        .all()

    return result


if __name__ == '__main__':
    print(select_6(3))
