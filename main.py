from src.models import Teacher, Discipline, Student, Group, Grade
import argparse

def create_record(args):
    # Логіка для створення запису в базі даних
    for _ in range(number_of_teachers):
            teacher = Teacher(fullname=fake.name())
            session.add(teacher)
        session.commit()


def read_records(args):
    # Логіка для відображення записів із бази даних
    pass

def update_record(args):
    # Логіка для оновлення запису в базі даних
    pass

def delete_record(args):
    # Логіка для видалення запису з бази даних
    pass

def main():
    parser = argparse.ArgumentParser(description='CLI програма для виконання CRUD операцій над базою даних.')
    
    subparsers = parser.add_subparsers(dest='action', help='Дія для виконання')
    
    # Підкоманда для операції create
    create_parser = subparsers.add_parser('create', help='Створення запису')
    create_parser.add_argument('-m', '--model', choices=['Teacher', 'Student', 'Discipline', 'Grade', 'Group'], help='Модель для створення')
    create_parser.set_defaults(func=create_record)
    
    # Підкоманда для операції read
    read_parser = subparsers.add_parser('read', help='Відображення записів')
    read_parser.add_argument('-m', '--model', choices=['Teacher', 'Student', 'Discipline', 'Grade', 'Group'], help='Модель для відображення')
    read_parser.set_defaults(func=read_records)
    
    # Підкоманда для операції update
    update_parser = subparsers.add_parser('update', help='Оновлення запису')
    update_parser.add_argument('-m', '--model', choices=['Teacher', 'Student', 'Discipline', 'Grade', 'Group'], help='Модель для оновлення')
    update_parser.set_defaults(func=update_record)
    
    # Підкоманда для операції delete
    delete_parser = subparsers.add_parser('delete', help='Видалення запису')
    delete_parser.add_argument('-m', '--model', choices=['Teacher', 'Student', 'Discipline', 'Grade', 'Group'], help='Модель для видалення')
    delete_parser.set_defaults(func=delete_record)
    
    args = parser.parse_args()
    
    if not hasattr(args, 'func'):
        parser.error('Не вказана дія (create, read, update, delete).')
    
    args.func(args)

if __name__ == '__main__':
    main()
