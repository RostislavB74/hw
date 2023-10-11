from datetime import date, datetime, timedelta
from random import randint, choice
import faker
from sqlalchemy import select

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session

"""
Створюємо свою ф-цію для отримання списку дат, у які відбувається навчальний процес.
Для спрощення викидаємо тільки дні, які потрапляють на вихідні.
"""


def date_range(start: date, end: date) -> list:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


"""
Функція створення БД, як параметр - передаємо шлях до файлу з SQL скриптом
"""

"""
Функція генерації фейкових даних і заповнення ними БД
"""


def fill_data():
    # Створюємо списки предметів і груп
    disciplines = [
        "Вища математика",
        "Фізичне виховання та самовдосконалення",
        "Фізика",
        "Комп'ютерні технології та програмування",
        "Ділова українська мова",
        "Фахова іноземна мова",
        "Вступ до спеціальності",
        "Екологія",
        "Електротехніка та авіоніка",
        "Теорія механізмів та машин",
        "Інженерна та комп'ютерна графіка",
        "Робочі тіла рідинно-газових систем ЛА",
        "Аналітичні та варіаційні методи",
        "Філософія",
        "Аерогідродинаміка та динаміка польоту",
        "Механіка матеріалів та конструкцій",
        "Гідравлічна і пневматична автоматика",
        "Історія України",
        "Теорія ймовірності"
    ]

    groups = ["АКФ 101", "АКФ 201", "АКФ 301", "АКФ 401", "АКФ 501",
              "АКФ 102", "АКФ 202", "АКФ 302", "АКФ 402", "АКФ 502",
              "АКФ 103", "АКФ 203", "АКФ 303", "АКФ 403", "АКФ 503"
              ]

    fake = faker.Faker('uk-UA')
    number_of_teachers = 15
    number_of_students = 150

    def seed_teachers():
        for _ in range(number_of_teachers):
            teacher = Teacher(fullname=fake.name())
            session.add(teacher)
        session.commit()

    def seed_disciplines():
        teacher_ids = session.scalars(select(Teacher.id)).all()
        for discipline in disciplines:
            session.add(Discipline(name=discipline,
                        teacher_id=choice(teacher_ids)))
        session.commit()

    def seed_groups():
        for group in groups:
            session.add(Group(name=group))
        session.commit()

    def seed_students():
        group_ids = session.scalars(select(Group.id)).all()
        for _ in range(number_of_students):
            student = Student(fullname=fake.name(), group_id=choice(group_ids))
            session.add(student)
        session.commit()

    def seed_grades():
        # дата початку навчального процесу
        start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
        # дата закінчення навчального процесу
        end_date = datetime.strptime("2023-05-25", "%Y-%m-%d")
        d_range = date_range(start=start_date, end=end_date)
        discipline_ids = session.scalars(select(Discipline.id)).all()
        student_ids = session.scalars(select(Student.id)).all()

        for d in d_range:  # пройдемося по кожній даті
            random_id_discipline = choice(discipline_ids)
            random_ids_student = [choice(student_ids) for _ in range(5)]
            # проходимося списком "везучих" студентів, додаємо їх до результуючого списку
            # і генеруємо оцінку
            for student_id in random_ids_student:
                grade = Grade(
                    grade=randint(1, 12),
                    date_of=d,
                    student_id=student_id,
                    discipline_id=random_id_discipline,
                )
                session.add(grade)
        session.commit()

    seed_teachers()
    seed_disciplines()
    seed_groups()
    seed_students()
    seed_grades()


if __name__ == "__main__":
    fill_data()
