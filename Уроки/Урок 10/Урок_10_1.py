import sqlite3

connection = sqlite3.connect("Library.sl3", 5)
cur = connection.cursor()

# cur.execute("CREATE TABLE first_table (name TEXT)") #Створення таблиці
# cur.execute("INSERT INTO first_table (name) VALUES ('Kate')") #Додали дані
# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=2") #Отримали дані
# cur.execute("UPDATE first_table SET name='Anny' WHERE rowid=3") #Змінити дані
# cur.execute("DELETE FROM first_table WHERE rowid=4") #Видалення даних
# cur.execute("SELECT rowid, name FROM first_table") #Щоб повернуло в термінал дані
connection.commit()

res = cur.fetchall()
print(res)
connection.close()