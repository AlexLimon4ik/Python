import sqlite3

connection = sqlite3.connect("FruitBasket.sl3", 5)
cur = connection.cursor()

# Таблицю робимо
cur.execute("CREATE TABLE Fruits (name TEXT, color TEXT)")

cur.execute("INSERT INTO Fruits (name, color) VALUES ('Яблуко', 'Червоне')")
cur.execute("INSERT INTO Fruits (name, color) VALUES ('Банан', 'Жовтий')")
cur.execute("INSERT INTO Fruits (name, color) VALUES ('Апельсин', 'Помаранчевий')")

# Завдання роблю
cur.execute("UPDATE Fruits SET color='Зелене' WHERE name='Яблуко'")
cur.execute("SELECT color, name FROM Fruits WHERE color='Жовтий'")
cur.execute("SELECT rowid, name, color FROM Fruits") 

# Відправляю це все
connection.commit()

res = cur.fetchall() # а це щоб останю задачу вивело
print(res)

connection.close()
