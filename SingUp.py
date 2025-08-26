import subprocess
import time
import sys
import json
from datetime import datetime
def  read_non_empty_value(user_variable):
    read_value = input(f'\nCreate a {user_variable} name: ')
    while read_value == '':
        print(f'\nThe name of {user_variable} cannot be empty!')
        read_value = input(f'Create a {user_variable} name: ')
    return read_value
def  read_password_value(password_variavel):
    read_value = input(f'\nCreate a {password_variable} for the user: ')
    while read_value == '':
        print(f'\n{password_variable} cannot be empty!')
        read_value = input(f'Create a {password_variable} for the user: ')
    return read_value
def check_valid_birthday(birthday_text):
    try:
        valid_birthday = datetime.strptime(birthday_text, "%d/%m/%Y")
        return True
    except:
        return False
def read_valid-birthday():
    birthdayString = input('\nEnter your birthday: ')
    while not check_valid_birthday(birthdayString):
        print('\nInvalid!')
        birthdayString = input('Enter your birthday: ')
    birthday = datetime.strptime(birthdayString, "%d/%m/%Y")
    print()
    return birthday
def loading():
    dots = ['.', '.', '.']
    for dot in dots:
        sys.stdout.write(dot)
        sys.stdout.flush()
        time.sleep(1)
def read_Account( user_list):
    while True:
        user =  read_non_empty_value('user')
        if check_user_exists(user,  user_list):
            print("\nErro: This username is already in use. Please choose another one..\n")
        else:
            break
    password =  read_password_value('password')
    birthday = read_valid-birthday()
    account = {
        'user': user,
        'password': password,
        'birthday': birthday.strftime('%d/%m/%Y'),
    }
    print('______________________________')
    print('\naccount criada!\n\nRedirecting', end='')
    loading()
    return account
def check_user_exists(user,  user_list):
    for account in  user_list:
        if account['user'] == user:
            return True
    return False

def read_json():
    with open("accounts.json", "r") as my_file:
        users_list = json.load(my_file)
    return users_list

def  save_json(list):
    with open("accounts.json", "w") as my_file:
        list_json = json.dumps(users_list, indent=4)
        my_file.write(list_json)
users_list = read_json()
for i in range(1):
    my_user = read_Account(users_list)
    users_list.append(my_user)
     save_json(users_list)
    subprocess.run(["python", "MainMenu.py"])
    exit()
