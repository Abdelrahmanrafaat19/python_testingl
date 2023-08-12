import sqlite3

db = sqlite3.connect("newDataBase.db")
cr = db.cursor()
cr.execute("create table if not exists tnew(name text,lname text)")
cr.execute("insert into tnew (name,lname) values ('Abdelrahman','shoaib')")
db.commit()
