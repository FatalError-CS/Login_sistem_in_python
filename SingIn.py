import subprocess
import time
import json
import sys
def  read_non_empty_value(user_variable):
    read_value = input(f'\nEnter the name of {user_variable}: ')
    while read_value == '':
        print(f'\nThe name of {user_variable} cannot be empty!')
        read_value = input(f'\nEnter the name of {user_variable}: ')
    return read_value
def  read_password_value(variable_password):
    read_value = input(f'\nEnter the users {variable_password}: ')
    while read_value == '':
        print(f'\n{variable_password} cannot be empty!')
        read_value = input(f'\nEnter the users {variable_password}: ')
    return read_value
def loading():
    dots = ['.', '.', '.']
    for dot in dots:
        sys.stdout.write(dot)
        sys.stdout.flush()
        time.sleep(1)
def  check_login(user_list):
    user =  read_non_empty_value('user')
    password =  read_password_value('password')
    for account in user_list:
        if account['user'] == user and account['password'] == password:
            print('______________________________')
            print('\nLogin successful!\n\nRedirecting', end='')
            loading()
            return True
    print('______________________________')
    print("\nErro:Incorrect username or password!\n\nTry again")
    print('______________________________\n')
    return False
def read-json():
    with open("accounts.json", "r") as  my_file:
        user_list = json.load( my_file)
    return user_list
def login():
    user_list = read-json()
    while True:
        user_logged =  check_login(user_list)
        if user_logged:
            subprocess.run(["python", "MainMenu.py"])
            return user_logged
user_logged = login()
