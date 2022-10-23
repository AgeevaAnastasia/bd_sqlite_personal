# первое заполнение базы, запускать один раз!

import sqlite3
bd = sqlite3.connect('data_base.db')
cursor = bd.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
               id INTEGRER, 
               first_name TEXT, 
               last_name TEXT,
               position TEXT,
               salary INTEGER,
               bonus INTEGER
               )''')
bd.commit()


base = [(1, 'Иван', 'Иванов', 'главный инженер', 50000, 12000),
        (2, 'Игорь', 'Семенов', 'инженер', 40000, 10000),
        (3, 'Олег', 'Петров', 'завхоз', 12000, 3000)]
        

try:
    cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)', base)
    bd.commit()
except:
    print('Данные уже есть')