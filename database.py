import sqlite3
connection = sqlite3.connect('files/users.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
incity TEXT NOT NULL,
country TEXT NOT NULL,
vzr TEXT NOT NULL,
deti TEXT NOT NULL,
hotel TEXT NOT NULL,
pitanie TEXT NOT NULL,
nochi TEXT NOT NULL,
name TEXT NOT NULL,
email TEXT NOT NULL,
data TEXT NOT NULL,
)
''')

cursor.execute('INSERT INTO users(data, incity, country, vzr, deti, hotel, pitanie, nochi, name, email)VALUES(??????????)',
               ())

connection.commit()
connection.close()

cursor.execute("CREATE TABLE IF NOT EXISTS block(id INT); ")


def add(id):
    if (id,) in get_id(): return
    cur.execute(f"INSERT INTO users VALUES({id});")
    conn.commit()

def get_all():
    s = cur.execute("SELECT * FROM users;").fetchall()
    conn.commit()
    return s

def count():
    s = cur.execute("SELECT COUNT(*) FROM users;").fetchone()
    conn.commit()
    return s[0]

def get_id():
    s = cur.execute("SELECT id FROM users;").fetchall()
    conn.commit()
    return s

def check_block(id):
    s = cur.execute("SELECT * FROM block; ").fetchall()
    conn.commit()
    return (id,) in s

def block(id):
    cur.execute(f"INSERT INTO block VALUES({id}); ").fetchall()
    conn.commit()

def delete(id):
    cur.execute(f"DELETE FROM block WHERE id = {id}; ").fetchall()
    conn.commit()
