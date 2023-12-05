
import sqlite3
connection = sqlite3.connect('library.db')
cursur = connection.cursor()

cursur.execute("""CREATE TABLE IF NOT EXISTS USER
               (
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NAME TEXT NOT NULL,
                USER_NAME TEXT NOT NULL,
                PASSWORD  NOT NULL UNIQUE
              
               )""")


cursur.execute("""CREATE TABLE IF NOT EXISTS BOOKS
               (
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                BOOK_AUTHOR TEXT NOT NULL,
                BOOK_NAME TEXT NOT NULL,
                PUBLICTION_DATE  NOT NULL 
              
               )""")

cursur.execute("""CREATE TABLE IF NOT EXISTS LIBRARIAN
               (
                
                LIBRARIAN_NAME TEXT NOT NULL,
                LIBRARIAN_USER_NAME TEXT UNIQUE NOT NULL,
                PASSWORD TEXT NOT NULL UNIQUE,
                PHONE_NUMBER INTERGER NOT NULL
                
               )""")
print("successfully create table")
# cursur.execute("INSERT INTO USER(NAME,USER_NAME,PASSWORD) VALUES('VICKY','VIKRAM','VIKRAM123')")

def LOG_IN(USER_NAME,PASSWORD):
    cursur.execute("SELECT PASSWORD FROM USER WHERE USER_NAME=(?)",USER_NAME)
    PASSWORD1=cursur.fetchone()
    if PASSWORD1 in PASSWORD:
       return True
    return False

def BOOK_USER():
  cursur.execute ("INSERT INTO USER(NAME,USER_NAME,PASSWORD) VALUES (?,?,?)")
  connection.commit()
  return True

def BOOKS_INFO(DATA):
  cursur.execute("INSERT INTO BOOKS(BOOK_AUTHOR , BOOK_NAME, PUBLICTION_DATE ) VALUES(?,?,?)",DATA)
  connection.commit
  return True

def BOOK_RECIVER(DATA):
  cursur.execute ("INSERT INTO BOOKS VALUES(?,?,?)",DATA)
  connection.commit()
  return True


def USER_INFO():
  cursur.execute("SELECT*FROM USER")
  DATA=cursur.fetchall()
  return DATA

def UPDATE_BOOK_USER(DATA):
    cursur.execute("UPDATE BOOK_USER SET (NAME,USER_NAME,USER_PASSWORD)=(?,?,?) WHERE USERNAME = (?)",DATA)
    connection.commit()


def DELETE_BOOK_USER(USER_NAME):
   cursur.execute("DELETE FROM USER WHERE USER_NAME=(?)",USER_NAME)
   connection.commit
   
