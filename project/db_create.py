#project/db_create.py

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

	#get a cusor jobect used to execute sql code

	c = connection.cursor()

	#create the table
	c.execute("""CREATE TABLE IF NOT EXISTS tasks
					(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
					name TEXT NOT NULL, due_date TEXT NOT NULL,
					priority INTEGER NOT NULL, status INTEGER NOT NULL)
				""")

	#insert dummy data into the table
	c.execute("""INSERT INTO tasks(name, due_date, priority, status) VALUES("Finish Real Python 2 Course", "03/25/2017", 10, 1)""")
	c.execute("""INSERT INTO tasks(name, due_date, priority, status) VALUES("Finish this app", "02/25/2017", 10, 1)""")