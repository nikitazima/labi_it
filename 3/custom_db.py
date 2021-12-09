import os
import sqlite3


def create_db():
    if not os.path.exists('database.db'):
        conn = sqlite3.connect('database.db')
        curs = conn.cursor()
        curs.execute('CREATE TABLE users (username text , password text)')
        conn.commit()

def add_user(username , password):
    conn = sqlite3.connect('database.db')
    curs = conn.cursor()
    curs.execute('INSERT INTO users VALUES(? , ?)' , (username , password))
    conn.commit()

def check_user(username):
    conn = sqlite3.connect('database.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM users WHERE username = ?' , (username ,))
    if len(curs.fetchall()) != 0:
        return True
    return False

def get_by_username(username):
    conn = sqlite3.connect('database.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM users WHERE username = ?' , (username ,))
    return curs.fetchall()