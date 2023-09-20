import json

import psycopg2

import queries
from config import db_config


def create_tabel_with_data() -> None:
    """Функция создает таблицу в бд и заполняет её данными."""
    with conn as connection:
        with connection.cursor() as cursor:
            with open('data.json') as file:
                data = json.load(file)
                cursor.execute(queries.create_table_query)
                for obj in data:
                    cursor.execute(queries.insert_data, (obj['id'],
                                                         obj['ParentId'],
                                                         obj['Name'],
                                                         obj['Type'],
                                                         ),
                                   )


def find_employees(empl_id: int) -> str:
    """Функция возвращает сотрудников одного офиса."""
    with conn as connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.main_query, [empl_id])
            return ' '.join(list(map(lambda x: x[0], cursor.fetchall())))


if __name__ == '__main__':
    conn = psycopg2.connect(**db_config)

    create_tabel_with_data()

    employee_id = input('Введите id сотрудника: ')
    try:
        result = find_employees(int(employee_id))
        if result:
            print(result)
    except ValueError:
        print('Неверные данные')

    conn.close()
