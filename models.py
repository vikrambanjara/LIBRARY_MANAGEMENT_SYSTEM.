
import sqlite3
connection= sqlite3.connect('library managemaent.db')
cursor=connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS USERS
               (
                NAME TEXT NOT NULL,
                USER_NAME TEXT NOT NULL UNIQUE,
                PASSWORD TEXT NOT NULL,
                MOBILE_NO INT NOT NULL 
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS LIBRARIAN
               (
                NAME TEXT NOT NULL,
                USER_NAME TEXT NOT NULL UNIQUE,
                PASSWORD TEXT NOT NULL,
                MOBILE_NO INT NOT NULL              
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS BOOKS
               (
                AUTHOR TEXT NOT NULL,
                BOOK_NAME TEXT NOT NULL UNIQUE,
                PUBLICATION_COMPANY TEXT NOT NULL,
                RENTED_DATE DATE,
                RENTED_USER TEXT)""")         

def librarian_validation(user_name, password):
  cursor.execute("SELECT PASSWORD FROM LIBRARIAN WHERE USER_NAME=(?)",(user_name,))
  Password=cursor.fetchone()
  if password :
    if Password==None:
        return False

    elif password in Password:
      return True
    return False
  return False


def user_validation(username,password):
    cursor.execute("SELECT PASSWORD FROM USERS WHERE USER_NAME = (?)",(username,))
    Password = cursor.fetchone()
    if password:
        if Password==None:
            return False
        elif password in Password:
            return True
        return False
    return False
  

def add_librarian(data):
   cursor.execute("INSERT INTO LIBRARIAN VALUES(?,?,?,?)",data)
   connection.commit()
   
def add_user(data):
   cursor.execute("INSERT INTO USERS VALUES(?,?,?,?)",data)
   connection.commit()

   
def add_book(data):
    cursor.execute("INSERT INTO BOOKS (AUTHOR,BOOK_NAME,PUBLICATION_COMPANY) VALUES(?,?,?)",data)
    connection.commit()
    
    
def update_user_details(data):
    cursor.execute("UPDATE USERS SET (NAME,USER_NAME,PASSWORD,MOBILE_NO) = (?,?,?,?) WHERE USER_NAME = (?)",data)
    connection.commit()
    

def update_book_details(data):
    cursor.execute("UPDATE BOOKS SET (AUTHOR,BOOK_NAME,PUBLICATION_COMPANY) = (?,?,?) WHERE BOOK_NAME = (?)",data)
    connection.commit()
    

def get_user(username):
    cursor.execute("SELECT * FROM USERS WHERE USER_NAME=(?)",(username,))
    check = cursor.fetchone()
    return check


def get_librarian(username):
    cursor.execute("SELECT * FROM LIBRARIAN WHERE USER_NAME=(?)",(username,))
    check = cursor.fetchone()
    return check



def delete_user(username):
    if get_user(username):
        cursor.execute("DELETE FROM USERS WHERE USER_NAME = (?)",(username,))
        connection.commit()
        return True
    return False

def get_book(book_name):
    cursor.execute("SELECT * FROM BOOKS WHERE BOOK_NAME=(?)",(book_name,))
    check = cursor.fetchone()
    return check

def delete_book(book_name):
    if get_book(book_name):
        cursor.execute("DELETE FROM BOOKS WHERE BOOK_NAME = (?)",(book_name,))
        connection.commit()
        return True
    
def rented_book(data):
    cursor.execute("UPDATE BOOKS SET (RENTED_DATE,RENTED_USER) = (?,?) WHERE BOOK_NAME = (?) ",data)
    connection.commit()
    return True

def rented_out_book(book_name):
    cursor.execute("UPDATE BOOKS SET (RENTED_DATE,RENTED_USER) = (?,?) WHERE BOOK_NAME = (?) ",(None,None,book_name))
    connection.commit()
    return True