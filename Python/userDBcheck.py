import time
import subprocess

file_path = 'your\path\to\database.db'
subprocess.run(['del', file_path], shell=True)  # Windows example
#connecting to database
import sqlite3
basefile = 'your\path\to\database.db'
con = sqlite3.connect(basefile)
cur = con.cursor()

# Step 2: Create a table
# Tables store data in rows and columns. setting empty database
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT UNIQUE
);
'''
cur.execute(create_table_query)
print("Database set.")
#writing database
do = 1
wrong_try = 4
usrnm = str(input("Usr: "))
passwd = str(input("passwd: "))
role = "user"

if usrnm == "admin" and passwd == "admin":
    do = 1
    role = "administrator"
    insert_data_query = '''INSERT INTO users (username,password,role) VALUES (?,?,?);'''

    user_data = [
        (usrnm, passwd, role)
    ]

    cur.executemany(insert_data_query,user_data)
    con.commit()
    print("Changes Commited.")


elif usrnm == "" or passwd == "":
    print("\n You cannot perform this action.")
    time.sleep(1)
    print("Exiting from program.")
    do = 0
    
else:
    do = 1
    insert_data_query = '''INSERT INTO users (username,password,role) VALUES (?,?,?);'''

    user_data = [
        (usrnm, passwd, role)
    ]

    cur.executemany(insert_data_query,user_data)
    con.commit()
    print("Changes Commited.")


#getting database

select_usrs = '''SELECT username,password,role FROM users;'''
cur.execute(select_usrs)
rows = cur.fetchall()
    #print("\n User Data's: ")
    #for row in rows:
    #    print(f"usrname:{row[0]},passwd:{row[1]},accrole:{row[2]}")

while(do == 1):
            
        print("\n---Login Section---\n")

        usrinp = str(input("username: "))
        passinp = str(input("password: "))
        if(usrinp == "" or passinp == ""):
            print("\n You cannot perform this action.")
            wrong_try -= 1
            if(wrong_try <= 0):
                 wrong_try = 0
                 do = 0
            continue
        for row in rows:
            if(usrinp == row[0] and passinp == row[1]):
                print(f"\nWelcome Your role is {row[2]} in this site.\n")
                do = 0
                time.sleep(1)
                break
            else:
                print("\nWrong username or password please try again.\n")

                time.sleep(1)
                do = 1

con.close()
