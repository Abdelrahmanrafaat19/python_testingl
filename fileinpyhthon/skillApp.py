import sqlite3
import timeit

my_massege = """
Enter Your Charchter
s=>Show data From DataBase
i=>Insert data to DataBase
d=>delete data From DataBase
u=>updata data in Data Base by ID
"""
print(my_massege)

db = sqlite3.connect("MySkillsApp.db")
cursor = db.cursor()
# Create the Skills Table
cursor.execute(
    "Create table if not exists MySkills(name text,lastname text,phoneNumber text)"
)

user_char = input("Insert Your Charcter:")


def get_all_data():
    print("Show Data")


def update_data():
    print("updata data")


def insert_data():
    try:
        name = input("Enter Your First name:")
        lastname = input("Enter Your Last name:")
        phoneNumber = input("Enter Your Phone Number:")
        cursor.execute(
            f"insert into MySkills(name,lastname,phoneNumber) values ('{name}','{lastname}','{phoneNumber}')"
        )
        print("the Data Added Scusses")
    except:
        print("The Error in Insert Your Data")


def delet_data():
    print("delet Data")


while user_char.lower() != "n":
    if user_char.lower() == "s":
        get_all_data()
    elif user_char.lower() == "u":
        update_data()
    elif user_char.lower() == "d":
        delet_data()
    elif user_char.lower() == "i":
        insert_data()
    else:
        print("You Are Insert Wrong Chater")
    user_char = input("Insert Your Charcter:")


db.commit()
print(
    timeit.timeit("'hellopeaple'"),
    "sqlite3",
)
