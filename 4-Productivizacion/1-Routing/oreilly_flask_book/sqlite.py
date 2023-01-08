'''
1. Creamos la conextion con la BD + cursor
2. Creamos una tabla
3. Insertamos un usuario
4. Cerramos conexion
5. Insertamos varios usuarios

'''
import sqlite3

connection = sqlite3.connect('data.db')

# Para seleccionar y empezar cosas con el DB. Ejecuta las queries
# y almacena el resultado
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, name text, password text)"

cursor.execute(create_table)

# Insertamos un usuario en la BD
user = (1, 'dani', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'bob', 'wjsh'),
    (3, 'ann', 'ohnj')
]
cursor.executemany(insert_query, users)

# Para seleccionar los usuarios
select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)


# Cuando insertemos datos, hay que decirle al connect que los guarde
# en la BD.
connection.commit()

# Cerramos las conextion con la BD
connection.close()