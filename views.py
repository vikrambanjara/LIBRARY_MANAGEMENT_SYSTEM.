

import controler
import models
import datetime



def librarian_func():
   print("Enter 1 For Add Librarian")
   print("Enter 2 For Add User")
   print("Enter 3 For Add Book")
   print("Enter 4 For Update User Details")
   print("Enter 5 For Update Book details")
   print("Enter 6 For Delete User")
   print("Enter 7 For delete Book")
   print("Enter Othey key For Exit")



def user_func():
   print("ENTER 1 FOR RENT A BOOK")
   print("ENTER 2 FOR RENT OUT BOOK")
   print("ENTER ANY KEY FOR EXIT")

def user_key(n,user_name):
   if n==1:
      rent_book(user_name)
   elif n==2:
      rent_out_book(user_name)
   else:
      print("invalid choose")


def librarian_key(n):
   if n==1:
      add_librarian()

   elif n == 2:
        add_user()  

   elif n == 3:
        add_book()
        
   elif n == 4:
        update_user_details()
        
   elif n == 5:
        update_book_details()
        
   elif n == 6:
        delete_user()
        
   elif n == 7:
        delete_book()

   else:
       print("invalid choice")
        

def add_librarian():
    name = input("Enter Librarian Name : ")
    username = input("Create Librarian Username : ")
    password = input("Create Password : ")
    mobile_no = input("Enter Mobile_No : ")
    data = (name,username,password,mobile_no)
    controler.cheak_librarian(data)



def add_user():
    name = input("Enter User Name : ")
    username = input("Create User Username : ")
    password = input("Create Password : ")
    mobile_no = input("Enter Mobile_No : ")
    data = (name,username,password,mobile_no)
    controler.cheak_user(data)

def add_book():
    author = input("Enter Author Name : ")
    book_name = input("Enter Book Name : ")
    publication_company = input("Enter Publication Company : ")
    data = (author,book_name,publication_company)
    controler.check_book(data)

def update_user_details():
    username = input("Enter current username : ")
    new_name = input("Enter New Name : ")
    new_username = input("Enter New Username : ")
    new_password = input("Create New Password : ")
    new_mobile_no = input("Enter New Mobile no. : ")
    data = (new_name,new_username,new_password,new_mobile_no,username)
    if controler.update_user_details(data,username):
        print("User Update successfully")
    

def update_book_details():
    book_name = input("Enter Book Name : ")
    new_author = input("Enter New Author Name : ")
    new_book_name = input("Enter New Book Name : ")
    new_publication_company = input("Enter New Publication Company : ")
    data = (new_author,new_book_name,new_publication_company,book_name)
    if controler.update_book_details(data,book_name):
        print("Book Update successfully")
    

def delete_user():
    username = input("Enter Username For Delete User : ")
    if models.delete_user(username):
        print("User Delete Successfully")
    else:
        print("Username not exists")

def delete_book():
    book_name = input("Enter Book Name For Delete Book : ")
    if models.delete_book(book_name):
        print("Book Delete Successfully")
    else:
        print("Book Name Already not exists")


def rent_book(user_name):
   book_name=input("ENTER A BOOK NAME : ")
   current_date=datetime.datetime.now().date()
   data=(current_date,user_name,book_name)
   controler.cheak_rented_book(data,book_name)


def rent_out_book(user_name):
   book_name=input("ENTER A BOOK NAME : ")
   current_date=datetime.datetime.now().date()
   controler.cheak_out_book(book_name)


   

def admin_func():
    print("ENTER 1 FOR ADD LIBRARIAN ")
    print("ENTER 2 FOR ADD USER")
    print("ENTER ANY NO. FOR EXIT")

def admin_choice(choice):
    if choice==1:
        add_librarian()
    elif choice==2:
        add_user()
    else:
        print("invalid choice")
    

def main():
    user_name = input("Enter Your User_name : ")
    password = input("Enter Your Password : ")
    if controler.log_in(user_name,password):
        print("WELCOME TO THE LIBRARY ")
        admin_func()
        Choose=int(input("ENTER A NUMBER: "))
        admin_choice(Choose)
    elif models.librarian_validation(user_name,password):
        print("welcome to library")
        librarian_func()
        Choose=int(input("ENTER A NUMBER: "))
        librarian_key(Choose)
    elif models.user_validation(user_name,password):
        print("welcome to the library")
        user_func() 
        Choose=int(input("ENTER A NUMBER: "))   
        user_key(Choose,user_name)
    else:
        print("wrong username and password")

main()