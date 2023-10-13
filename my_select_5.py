from src.models import Teacher, Discipline
from src.db import session

"""Знайти які курси читає певний викладач.
SELECT t.fullname  as 'Викладач', i.name as 'Предмет'
FROM items i 
JOIN teachers t ON t.id  = i.teachers_id  
WHERE t.id  = 15
ORDER BY t.fullname  """


def select_5(teachers_id):
    result = session.query(Teacher.fullname, Discipline.name) \
        .select_from(Discipline)\
        .join(Teacher)\
        .where(Discipline.teacher_id == Teacher.id)\
        .filter(Teacher.id == teachers_id)\
        .all()

    return result


if __name__ == '__main__':
    print(select_5(6))
