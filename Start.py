import subprocess
w = True
while w:
    print('______________________________')
    registro = input('\n|-Start menu-|\n\n-Sing up\n-Sing in\n\n:')
    print('______________________________')
    if registro in ['sing up', '1', 'Sing up', 'singup', 'Singup']:
        w = False
        subprocess.run(["python", "SingUp.py"])
        exit()
    elif registro in ['Sing in', 'sing in', '2', 'Singin', 'singin']:
        w = False
        subprocess.run(["python", "SingIn.py"])
        exit()
    else:
        print('Invalid!')
