from dbms.qu import *  
from utility.getdata import *

def menu():
    p = QModel()  # Updated class instantiation
    while True:
        a = int(input("1.register\n2.update\n3.delete\n4.exit\n"))
        if a == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if p.register(username, password):
                print("User registered successfully.")
            else:
                print("Username already exists.")
        elif a == 2:
            old_username = input("Enter current username: ")
            old_password = input("Enter current password: ")
            if not p.check_password(old_username, old_password):
                print("Incorrect password.")
                continue
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            if p.update_user(old_username, new_username, new_password):
                print("User updated successfully.")
            else:
                print("Username does not exist.")
        elif a == 3:
            username = input("Enter username to delete: ")
            password = input("Enter password: ")
            if not p.check_password(username, password):
                print("Incorrect password.")
                continue
            if p.delete_user(username):
                print("User deleted successfully.")
            else:
                print("Username does not exist.")
        elif a == 4:
            print("Exiting...")
            break

