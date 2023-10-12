from sqlalchemy import func, desc, select, and_

from src.models import Group, Grade, Student, Discipline
from src.db import session


def select_one():
    """
   Знайти середній бал на потоці (по всій таблиці оцінок).
   SELECT ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
ORDER BY average_grade 

    """
    result = session.query(func.round(func.avg(Grade.grade), 2)) \
        .select_from(Grade)\
        .all()
    return result


if __name__ == '__main__':
    print(select_one())
