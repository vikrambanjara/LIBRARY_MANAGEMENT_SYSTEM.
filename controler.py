
import models
import datetime

def log_in(user_name,password):
  if user_name=='book' and password=='book':
    return True
  return False


def cheak_librarian(data):
  name,user_name,password,mobile_number=data
  
  if models.get_librarian(user_name):
    print("this user_name already exist")
  else:
    models.add_librarian(data)
    print("librarian add successfully")
    


def cheak_user(data):
  name,user_name,password,mobile_number=data
  if models.get_user(user_name):
      print("This username already exists")
  else:
    models.add_user(data)
    print("User add successfully")

def check_book(data):
    AUTHOR,BOOK_NAME,PUBLICATION_COMPANY=data
    if models.get_book(BOOK_NAME):
        print("This book already exists")
    else:
        models.add_book(data)
        print("Book add successfully")

       



def update_user_details(data,username):
    if models.get_user(username):
        models.update_user_details(data)
        return True
    else:
        print("User Not Found")


def update_book_details(data,book_name):
    if models.get_book(book_name):
        models.update_book_details(data)
        return True
    else:
        print("Book Not Found")

def cheak_rented_book(data,book_name):
   if models.get_book(book_name):
      models.rented_book(data)
      print("Rented book successfully")
   else:
      print("This book is not exits")


def cheak_out_book(book_name):
   if models.get_book(book_name):
      models.rented_out_book(book_name)
      print("Rent out book successfully")
   else:
      print("This book is not exits")
      

      