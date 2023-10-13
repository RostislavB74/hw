from sqlalchemy import func, and_, select

from src.models import Teacher, Discipline, Grade
from src.db import session

"""Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN teachers t ON t.id = g.grade 
GROUP  BY t.fullname
--ORDER BY average_grade DESC 
def select_last(discipline_id, group_id):
    subquery = (select(Grade.date_of).join(Student).join(Group).where(
        and_(Grade.discipline_id == discipline_id, Group.id == group_id)
    ).order_by(desc(Grade.date_of)).limit(1).scalar_subquery())

    r = session.query(Discipline.name,
                      Student.fullname,
                      Group.name,
                      Grade.date_of,
                      Grade.grade
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group)\
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id, Grade.date_of == subquery)) \
        .order_by(desc(Grade.date_of)) \
        .all()
    return r
"""


def select_8(teacher_id):
    subquery = (select(Grade.grade).join(Discipline).join(Teacher).where(
        and_(Grade.discipline_id == Discipline.id, Teacher.id == Discipline.teacher_id)
    ).filter(Teacher.id== teacher_id).scalar_subquery())
    result = session.query(Teacher.fullname, func.round(func.avg(Grade.grade), 2)) \
        .select_from(Grade)\
        .join(Discipline)\
        .join(Teacher)\
        .filter(Teacher.id==subquery)\
        .all()
        

    return result


if __name__ == '__main__':
    print(select_8(8))
