
import sqlite3
# bd = sqlite3.connect('data_base.db')
# cursor = bd.cursor()
from controller import * 

# cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
#                id INTEGRER,
#                first_name TEXT,
#                last_name TEXT,
#                position TEXT,
#                salary INTEGER,
#                bonus INTEGER
#                )''')
# bd.commit()


def input_choice():
    while True:
        user_choice = input('1 - посмотреть базу \n'
                            '2 - добавить запись \n'
                            '3 - найти по ФИО \n'
                            '4 - удалить запись \n'
                            '5 - упорядочить по размеру зарплаты \n'
                            '6 - упорядочить по размеру премии \n'
                            '7 - изменить размер зарплаты \n'
                            '8 - изменить размер премии \n'
                            '9 - изменить должность \n'
                            '10 - вычислить среднюю зарплату \n'
                            '11 - вычислить среднюю премию \n'
                            'Для выхода нажмите <q>')
        if user_choice == '1':
            preview_base()
        elif user_choice == '2':
            add_record()
        elif user_choice == '3':
            find_record(input('Введите фамилию для поиска: '))
        elif user_choice == '4':
            delete_record(int(input('Введите id для удаления записи: ')))
        elif user_choice == '5':
            range_salary()
        elif user_choice == '6':
            range_bonus()
        elif user_choice == '7':
            set_salary(int(input('Введите id: ')),
                       int(input('Введите новый размер заработной платы: ')))
        elif user_choice == '8':
            set_bonus(int(input('Введите id: ')),
                      int(input('Введите новый размер премии: ')))
        elif user_choice == '9':
            set_position(int(input('Введите id: ')),
                         input('Введите новую должность: '))
        elif user_choice == '10':
            average_salary()
        elif user_choice == '11':
            average_bonus()
        elif user_choice == 'q':
            print('Выход')
            break
        else:
            print('Неверный ввод')


input_choice()
