import dbcreds
import mariadb
import dbconnect
import traceback

# Option 1: Write a new exploit


def newExploit():
    conn = dbconnect.get_db_connection()
    cursor = dbconnect.get_db_cursor(conn)
    if(conn == None or cursor == None):
        print("Error in database connection!")
        dbconnect.close_db_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return
    try:
        content = input("Enter exploit content here: ")
        cursor.execute(
            f"INSERT INTO exploits(user_id, content) VALUES('{user_id}', '{content}')")
        conn.commit()
    except:
        print("Failed to add new exploit")
        traceback.print_exc()
    dbconnect.close_db_cursor(cursor)
    dbconnect.close_db_connection(conn)


def viewMyExploits():
    conn = dbconnect.get_db_connection()
    cursor = dbconnect.get_db_cursor(conn)
    if(conn == None or cursor == None):
        print("Error in database connection!")
        dbconnect.close_db_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return
    try:
        cursor.execute(
            f"SELECT user_id, id, content FROM exploits WHERE user_id = '{user_id}'")
        content_rows = cursor.fetchall()
        for content in content_rows:
            print(
                f"ID: {content[0]}   User ID: {content[1]}     Content: {content[2]}")
    except:
        print("Failed to view user exploits")
        traceback.print_exc()
    dbconnect.close_db_cursor(cursor)
    dbconnect.close_db_connection(conn)


def viewAllOtherExploits():
    conn = dbconnect.get_db_connection()
    cursor = dbconnect.get_db_cursor(conn)
    if(conn == None or cursor == None):
        print("Error in database connection!")
        dbconnect.close_db_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return
    try:
        cursor.execute(
            f"SELECT user_id, id, content FROM exploits WHERE user_id != '{user_id}'")
        content_rows = cursor.fetchall()
        for content in content_rows:
            print(
                f"ID: {content[0]}   User ID: {content[1]}     Content: {content[2]}")
    except:
        print("Failed to view all other exploits!")
        traceback.print_exc()
    dbconnect.close_db_cursor(cursor)
    dbconnect.close_db_connection(conn)


def checkLogin():
    if(user_id == 1 or 2 or 3 or 4):
        print("---------------------")
        print(f"Welcome back {Username}!")
        print("---------------------")
        print("Select from 4 options:")
        print("---------------------")
        print("Enter a new exploit: 1")
        print("See all of your exploits: 2")
        print("See all other exploits: 3")
        print("Exit the application: 4")
        print("---------------------")
        return True
    elif(user_id == None):
        print("Error logging in, username and/or password is incorrect!")
        return False


while True:

    print("Please login by entering your username and password")
    print("---------------------")
    username = input("Username: ")
    password = input("Password: ")

    if(username == "Neo" and password == "neo123"):
        user_id = 1
    elif(username == "Morpheus" and password == "morpheus123"):
        user_id = 2
    elif(username == "Trinity" and password == "trinity123"):
        user_id: 3
    elif(username == "Agent Smith" and password == "smith123"):
        user_id = 4
    else:
        user_id = None

    if(user_id == 1):
        Username = "Neo"
    elif(user_id == 2):
        Username = "Morpheus"
    elif(user_id == 3):
        Username = "Trinity"
    elif(user_id == 4):
        Username == "Agent Smith"
    else:
        user_id = None

    checkLogin()
    selection = input("Please enter your selection: ")
    intSelection = int(selection)
    if(intSelection == 1):
        newExploit()
    elif(intSelection == 2):
        viewMyExploits()
    elif(intSelection == 3):
        viewAllOtherExploits()
    elif(intSelection == 4):
        break
    else:
        print("Invalid selection!")
