from sqlalchemy import func, desc, select, and_

from src.models import Student, Discipline, Grade, Group
from src.db import session

"""Знайти середній бал у групах з певного предмета."""


def select_last(group_id, discipline_id):
    subquery = (select(Grade).join(Group).where(
        and_(Grade.discipline_id == discipline_id, Group.id == group_id)
    ))

    r = session.query(Discipline.name,
                      Group.name,
                      func.round(func.avg(Grade.grade), 2).label('avg_grade')
                      ) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Group)\
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id)) \
        .order_by(desc(Group.id)) \
        .all()
    return r


if __name__ == '__main__':
    print(select_last(1, 2))

# def select_one():
#     """
#     Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
#     :return: list[dict]
#     """
#     result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
#         .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
#     return result
# if __name__ == '__main__':
#     print(select_one())
