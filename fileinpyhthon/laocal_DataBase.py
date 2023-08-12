import sqlite3

# Connect With Database
db = sqlite3.connect("CLS.db")
cr = db.cursor()
# Create Table in Database
cr.execute(
    "Create table if not exists myData (name text,lastname text,phonNumber text)"
)
# listToDataBase = ["Abdelrahman", "Abdelleh", "Mohammed", "Amir"]
# listToDatalBase = ["shoaib", "Shoaib", "Eid", "Agour"]
# listToDataPHBase = ["01006191527", "01063103655", "01063103655", "01235541558"]
# # Insert in DataBase
# for name, lastname, phoneNumber in zip(
#     listToDataBase, listToDatalBase, listToDataPHBase
# ):
#     cr.execute(
#         f"insert into myData(name,lastname,phonNumber) values ('{name}','{lastname}','{phoneNumber}')"
#     )
# # get All Data From DataBase
# listDataBase = cr.execute("select * from myData")
# for index in listDataBase:
#     for inde in index:
#         print(inde)

#     print(100 * "#")
# save Chandes
cr.execute("delete from myData where phonNumber = '01006191527'")
db.commit()
# Close The Database
db.close()
help(sqlite3.connect)
