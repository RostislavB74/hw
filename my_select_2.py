from sqlalchemy import func, desc

from src.models import Student, Discipline, Grade
from src.db import session
"""Знайти студента із найвищим середнім балом з певного предмета."""


def select_2(discipline_id: int):
    r = session.query(Discipline.name,
                      Student.fullname,
                      func.round(func.avg(Grade.grade), 2).label('avg_grade')
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Student.id, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .limit(1).all()
    return r


if __name__ == '__main__':
    print(select_2(3))
