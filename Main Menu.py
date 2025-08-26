import json
import time
import subprocessg
def ler_json():
    with open("accounts.json", "r") as my_file:
        user_list = json.load(my_file)
    return user_list

def save_jason(user_list):
    with open("accounts.json", "w") as my_file:
        json.dump(user_list, my_file, indent=4)

def print_account(user):
    print(f"\nuser: {user['user']}")
    print(f"password: {user['password']}")
    print(f"birthday: {user['birthday']}\n")
    
def print_users(user_list):
    if len(user_list) == 0:
        print("\nNo accounts found.\n\nCreate an account.")
        return
    for i, user in enumerate(user_list):
        print(f"\n====== {i + 1} ======")
        print_account(user)

def excluir_conta(user_list):
    if len(user_list) == 0:
        print("\nNo accounts found.\n\nCreate an account.")
        return
    
    print('______________________________')
    print("\nRegistered accounts:")
    for i, user in enumerate(user_list):
        print(f"\n{i + 1}. user: {user['user']}")
    
    select = int(input('\nEnter the account number you want to delete: ')) - 1
    if select < 0 or select >= len(user_list):
        print("Invalid account!")
        
    correct_password = user_list[select]['password']
    confirmation = input('\nEnter the users password to confirm the deletion.: ')

    if confirmation == correct_password:
        del user_list[select]
        save_jason(user_list)
        print('\nAccount successfully deleted!')
    else:
        print('\nInvalid Password!')

    
    save_jason(user_list)

def modify_information(user_list):
    if len(user_list) == 0:
        print("\nNo accounts found.\n\nCreate an account.")
        return

    print('______________________________')
    print("\nRegistered accounts:")
    for i, user in enumerate(user_list):
        print(f"\n{i + 1}. user: {user['user']}")

    index = int(input("\nEnter the account number you wish to modify:")) - 1
    if index < 0 or index >= len(user_list):
        print("\nInvalid account!")
        return

    mod = input('\nWhat information or information do you want to modify?:')
    if mod in ['nome', 'Nome']:
        user = input(f"\nEnter the new username: ")
        user_list[index]['user'] = user
    if mod in ['password', 'password']:
        password = input(f"\nEnter the new password: ")
        user_list[index]['password'] = password
    if mod in ['birthday', 'birthday']:
        birthday = input(f"\nEnter the new birthday: ")
        user_list[index]['birthday'] = birthday
        
    if mod in ['Name and password', 'name and password' 'Password and name', 'password and name']:
        user = input(f"\nEnter the new username: ")
        user_list[index]['user'] = user
        password = input(f"\nEnter the new password: ")
        user_list[index]['password'] = password
    if mod in ['Name and birthday', 'name and birthday', 'Birthday and name', 'birthday and name']:
        user = input(f"\nEnter the new username: ")
        user_list[index]['user'] = user
        birthday = input(f"\nEnter the new birthday: ")
        user_list[index]['birthday'] = birthday
    if mod in ['password and birthday', 'Password and birthday', 'Birthday and password', 'birthday and password']:
        password = input(f"\nEnter the new password: ")
        user_list[index]['password'] = password
        birthday = input(f"\nEnter the new birthday: ")
        user_list[index]['birthday'] = birthday

    save_jason(user_list)

    print("\nAccount updated successfully!")

def  play_game(user_list):
    if len(user_list) == 0:
        print("\nCreate an account to be able to play.")
        return
    else:
        subprocess.run(["python", "joguinho.py"])
        exit()

def logIn(user_list):
    if len(user_list) == 0:
        print("\nNo account to log in.\n\nCreate an account.")
        return
    else:
        subprocess.run(["python", "SingIn.py"])
        exit()

def menu():
    print('\n______________________________\n')
    print(f'Welcome')
    while True:
        print('______________________________\n')
         consultation = input('-Play(beta)\n-Check information about created accounts\n-Modify information\n-Delete account\n-Log in to another account\n-Create new account\n-Exit\n\n:')
        if  consultation in ['play', 'Play', '1']:
            user_list = ler_json()
             play_game(user_list)
            time.sleep(2)
        elif  consultation in ['Check information', 'Checkinformation', '2', 'checkinformation', 'Check information', 'Check', 'check']:
            user_list = ler_json()
            print_users(user_list)
            time.sleep(2)
        elif  consultation in ['modify', 'Modify', 'Modify information', 'modify information', 'Modifyinformation', 'modifyinformation', '3']:
            user_list = ler_json()
            modify_information(user_list)
            time.sleep(2)
        elif  consultation in ['Delete', 'delete', 'delete account', 'Delete account', 'deleteaccount', 'Deleteaccount', '4']:
            user_list = ler_json()
            excluir_conta(user_list)
            time.sleep(2)
        elif  consultation in ['Log in', 'log in', '5','Login', 'login']:
            user_list = ler_json()
            logIn(user_list)
            time.sleep(2)
        elif  consultation in ['Create', 'create', '6', 'Create account', 'create naccount', 'Createaccount', 'createnaccount']:
            subprocess.run(["python", "SingUp.py"])
            exit()
            time.sleep(2)
        elif  consultation in ['exit', 'Exit', '7']:
            exit()
            time.sleep(2)
        else:
            print('\nInvalid!')
            time.sleep(2)

menu()
