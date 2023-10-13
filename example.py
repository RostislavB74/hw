import argparse

# Імпорт необхідних модулів для роботи із базою даних

def create_record(model, data):
    print(data)
    

def read_records(model):
    # Логіка для відображення записів із бази даних
    pass

def update_record(model, data):
    # Логіка для оновлення запису у базі даних
    pass

def delete_record(model, record_id):
    # Логіка для видалення запису із бази даних
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI програма для виконання CRUD операцій над базою даних.')
    parser.add_argument('-a', '--action', choices=['create', 'read', 'update', 'delete'], help='Вибір дії (create, read, update, delete)', required=True)
    parser.add_argument('-m', '--model', help='Вказівка над якою моделлю проводити операцію', required=True)
    parser.add_argument('-d', '--data', help='Дані для створення або оновлення запису')
    parser.add_argument('-i', '--id', help='Ідентифікатор запису для операції update або delete')

    args = parser.parse_args()

    if args.action == 'create':
        create_record(args.model, args.data)
    elif args.action == 'read':
        read_records(args.model)
    elif args.action == 'update':
        if not args.id:
            parser.error('Для операції update необхідно вказати ідентифікатор запису (-i)')
        update_record(args.model, args.data)
    elif args.action == 'delete':
        if not args.id:
            parser.error('Для операції delete необхідно вказати ідентифікатор запису (-i)')
        delete_record(args.model, args.id)
