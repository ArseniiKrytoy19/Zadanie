import sqlite3
connection = sqlite3.connect('my_databse.db')
cursor = connection.cursor()
cursor.execute('SELECT MAX(age) FROM Users')
max_age = cursor.fetchone()[0]
print('Максимальный возраст среди пользователей:'. max_age)
connection.close()