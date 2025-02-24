import subprocess

w = True
while w:
    print('______________________________')
    registro = input('\n|-Menu inicial-|\n\n-Criar uma conta\n-Logar em uma existente\n\n:')
    print('______________________________')
    if registro in ['criar', '1', 'Criar', 'Criar uma conta', 'criar uma conta']:
        w = False
        subprocess.run(["python", "SingUp.py"])
        exit()
    elif registro in ['logar', 'Logar', '2', 'Logar em uma existente', 'logar em uma existente']:
        w = False
        subprocess.run(["python", "SingIn.py"])
        exit()
    else:
        print('Resposta valida invalida')
        