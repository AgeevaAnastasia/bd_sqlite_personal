import sqlite3
bd = sqlite3.connect('data_base.db')
cursor = bd.cursor()


def preview_base():
    print()
    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)
    print()

def add_record():
    base = [input("Введите id: "), input("Введите имя сотрудника: "),
            input("Введите фамилию сотрудника: "), 
            input("Введите должность сотрудника: "), 
            int(input("Введите зарплату сотрудника: ")), 
            int(input("Введите премию сотрудника: "))]
    cursor.execute('INSERT INTO personal VALUES(?,?,?,?,?,?)', base)
    bd.commit()

def find_record(text):
    cursor.execute('SELECT * FROM personal WHERE last_name LIKE (?)', (text,))
    one = cursor.fetchall()
    print()
    for i in one:
        print(*i)
    print()
    return one

def delete_record(id):
    cursor.execute('DELETE FROM personal WHERE id=:n;', {"n": id})
    bd.commit()


def range_salary():
    cursor.execute("SELECT * FROM personal ORDER BY salary DESC") 
    result = cursor.fetchall() 
    print()
    for i in result:
        print(*i)
    print()
    return result


def range_bonus():
    cursor.execute("SELECT * FROM personal ORDER BY bonus DESC") 
    result = cursor.fetchall() 
    print()
    for i in result:
        print(*i)
    print()
    return result


def set_salary(id, num):
    cursor.execute('UPDATE personal SET salary=:num WHERE id=:n;', {"num": num, "n": id})
    bd.commit()
    

def set_bonus(id, num):
    cursor.execute('UPDATE personal SET bonus=:num WHERE id=:n;', {"num": num, "n": id})
    bd.commit()


def set_position(id, pos):
    cursor.execute('UPDATE personal SET position=:pos WHERE id=:n;', {"pos": pos, "n": id})
    bd.commit()
    

def average_salary():
    lst = list(cursor.execute('SELECT salary FROM personal'))
    summ = 0
    for i in range(len(lst)):
        lst[i] = list(lst[i])
        summ += int(lst[i][0])
    avg = summ / len(lst)
    print()
    print(f'Средняя зарплата в компании сейчас равна {avg}')
    print()
    return avg


def average_bonus():
    lst = list(cursor.execute('SELECT bonus FROM personal'))
    summ = 0
    for i in range(len(lst)):
        lst[i] = list(lst[i])
        summ += int(lst[i][0])
    avg = summ / len(lst)
    print()
    print(f'Средняя премия в компании сейчас равна {avg}')
    print()
    return avg
