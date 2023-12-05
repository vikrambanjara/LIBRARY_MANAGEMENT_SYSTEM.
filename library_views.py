import library_models
import library_controler
import datetime

def func():
  print("enter 1 for log_in")
  print("enter 2 for book_reciver")
  print("enter 3 for get book_info")
  print("enter 4 for get user_info")
  print("enter 5 for upadte_Book_user")
  print("enter 6 for delete_book_user")
  print("enter any number for exit")

def func_choice(n):
  if n==1:
    USER_LOG_IN() 
  elif n==2:
    BOOK_RECIVER()
  elif n==3:
    BOOK_INFO()
  elif n==4:
    USER_INFO()
  # elif n==5:
  #   UPDATE_BOOK_USER()
  elif n==6:
    DELETE_BOOK_USER()
  else:
    print("Invalid choice")


def BOOK_RECIVER():
  USER_NAME=input("ENTER YOUR USER_NAME: ")
  PASSWORD=input("ENTER YOUR PASSWORD: ")
  RECEIVE_TIME=datetime.datetime.now().date()
  DATA=(USER_NAME,PASSWORD,RECEIVE_TIME)
  if library_models.BOOK_RECIVER(DATA):
    print("book_revcive successfully")
  return False


def BOOK_INFO():
  BOOK_AUTHOR=input("ENTER BOOK_AUTHOR NAME: ")
  BOOK_NAME=input("ENTER BOOK_NAME: ")
  PUBLICTION_DATE=input("ENTER PUBLICATION_DATE: ")
  DATA=(BOOK_AUTHOR,BOOK_NAME,PUBLICTION_DATE)
  if library_models.BOOKS_INFO(DATA):
    return DATA

def USER_INFO():
  USER_NAME=input("ENTER USER_NAME: ")
  DATA=library_models.USER_INFO(USER_NAME)
  return DATA


# def UPDATE_BOOK_USER():
  
    

def DELETE_BOOK_USER():
   USER_NAME=input("ENTER USER_NAME: ")
   library_models.DELETE_BOOK_USER(USER_NAME)
   print("Delete book user successfully")

def USER_LOG_IN():
   USER_NAME=input("ENTER YOUR USER_NAME: ")
   PASSWORD=input("ENTER YOUR PASSWORD: ")
   DATA=library_controler.LOG_IN(USER_NAME,PASSWORD)
   if DATA==1:
    USER_LOG_IN()
    print("LOG_IN SUCCESSFULLY")

    








