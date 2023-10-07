import sqlite3
from typing import List
import datetime
from model import Todo

conn = sqlite3.connect("todo.db")
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS todo (
        task text,
        category text,
        date_added text,
        date_completed text,
        status integer,
        position integer
    )""")

create_table()
