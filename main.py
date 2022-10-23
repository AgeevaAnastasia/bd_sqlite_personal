
import sqlite3
bd = sqlite3.connect('data_base.db')
cursor = bd.cursor()
from controller import * 

cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
               id INTEGRER, 
               first_name TEXT, 
               last_name TEXT,
               position TEXT,
               salary INTEGER,
               bonus INTEGER
               )''')
bd.commit()


def input_choice():
    while True:
        user_choice = input('1 - посмотреть базу \n2 - добавить запись \n3 - найти по ФИО \n4 - удалить запись \n5 - упорядочить по размеру зарплаты \n6 - упорядочить по размеру премии \n7 - изменить размер зарплаты \n8 - изменить размер премии \n9 - изменить должность \n10 - вычислить среднюю зарплату \n11 - вычислить среднюю премию \nДля выхода нажмите <q>')
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
            set_salary(int(input('Введите id: ')), int(input('Введите новый размер заработной платы: ')))
        elif user_choice == '8':
            set_bonus(int(input('Введите id: ')), int(input('Введите новый размер премии: ')))
        elif user_choice == '9':
            set_position(int(input('Введите id: ')), input('Введите новую должность: '))
        elif user_choice == '10':
            average_salary()
        elif user_choice == '11':
            average_bonus()
        elif user_choice == 'q':
            print('Выход')
            break
        else: print('Неверный ввод')

input_choice()
