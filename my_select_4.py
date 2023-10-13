from sqlalchemy import func

from src.models import Grade
from src.db import session


def select_4():
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
    print(select_4())
