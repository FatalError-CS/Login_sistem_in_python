import json
import time
import subprocess

def ler_json():
    with open("contas.json", "r") as meu_arquivo:
        lista_usuários = json.load(meu_arquivo)
    return lista_usuários

def salvar_json(lista_usuários):
    with open("contas.json", "w") as meu_arquivo:
        json.dump(lista_usuários, meu_arquivo, indent=4)

def imprimir_Conta(usuário):
    print(f"\nUsuário: {usuário['usuário']}")
    print(f"Senha: {usuário['senha']}")
    print(f"Data: {usuário['dataNascimento']}\n")
    
def imprimir_usuários(lista_usuários):
    if len(lista_usuários) == 0:
        print("\nNenhuma conta encontrada.\n\nCrie uma conta.")
        return
    for i, usuário in enumerate(lista_usuários):
        print(f"\n====== {i + 1} ======")
        imprimir_Conta(usuário)

def excluir_conta(lista_usuários):
    if len(lista_usuários) == 0:
        print("\nNenhuma conta encontrada.\n\nCrie uma conta.")
        return
    
    print('______________________________')
    print("\nContas registradas:")
    for i, usuário in enumerate(lista_usuários):
        print(f"\n{i + 1}. Usuário: {usuário['usuário']}")
    
    selecionar = int(input('\nDigite o número da conta que você deseja deletar: ')) - 1
    if selecionar < 0 or selecionar >= len(lista_usuários):
        print("Conta inválida!")
        
    senha_correta = lista_usuários[selecionar]['senha']
    confirmação = input('\nDigite a senha do usuário para confirmar a exclusão: ')

    if confirmação == senha_correta:
        del lista_usuários[selecionar]
        salvar_json(lista_usuários)
        print('\nConta excluida com sucesso!')
    else:
        print('\nSenha inválida!')

    
    salvar_json(lista_usuários)

def modificar_informacoes(lista_usuários):
    if len(lista_usuários) == 0:
        print("\nNenhuma conta encontrada.\n\nCrie uma conta.")
        return

    print('______________________________')
    print("\nContas registradas:")
    for i, usuário in enumerate(lista_usuários):
        print(f"\n{i + 1}. Usuário: {usuário['usuário']}")

    indice = int(input("\nDigite o número da conta que você deseja modificar:")) - 1
    if indice < 0 or indice >= len(lista_usuários):
        print("\nConta inválida!")
        return

    mod = input('\nQual informação ou informações desejas modificar?:')
    if mod in ['nome', 'Nome']:
        usuário = input(f"\nDigite o novo nome de usuário: ")
        lista_usuários[indice]['usuário'] = usuário
    if mod in ['Senha', 'senha']:
        senha = input(f"\nDigite a nova senha: ")
        lista_usuários[indice]['senha'] = senha
    if mod in ['Data', 'data']:
        data_nascimento = input(f"\nDigite a nova data de nascimento: ")
        lista_usuários[indice]['dataNascimento'] = data_nascimento
        
    if mod in ['Nome e senha', 'nome e senha' 'Senha e nome', 'senha e nome']:
        usuário = input(f"\nDigite o novo nome de usuário: ")
        lista_usuários[indice]['usuário'] = usuário
        senha = input(f"\nDigite a nova senha: ")
        lista_usuários[indice]['senha'] = senha
    if mod in ['Nome e data', 'nome e data', 'Data e nome', 'data e nome']:
        usuário = input(f"\nDigite o novo nome de usuário: ")
        lista_usuários[indice]['usuário'] = usuário
        data_nascimento = input(f"\nDigite a nova data de nascimento: ")
        lista_usuários[indice]['dataNascimento'] = data_nascimento
    if mod in ['Senha e data', 'senha e data', 'Data e senha', 'data e senha']:
        senha = input(f"\nDigite a nova senha: ")
        lista_usuários[indice]['senha'] = senha
        data_nascimento = input(f"\nDigite a nova data de nascimento: ")
        lista_usuários[indice]['dataNascimento'] = data_nascimento

    salvar_json(lista_usuários)

    print("\nConta atualizada com sucesso!")

def jogar_game(lista_usuários):
    if len(lista_usuários) == 0:
        print("\nCrie uma conta para poder jogar.")
        return
    else:
        subprocess.run(["python", "joguinho.py"])
        exit()

def logar(lista_usuários):
    if len(lista_usuários) == 0:
        print("\nNenhum conta para logar.\n\nCrie uma conta.")
        return
    else:
        subprocess.run(["python", "SingIn.py"])
        exit()

def menu():
    print('\n______________________________\n')
    print(f'Bem-vindo')
    while True:
        print('______________________________\n')
        consulta = input('-Jogar(beta)\n-Consultar informações das contas criadas\n-Modificar informações\n-Excluir conta\n-Logar em outra conta\n-Criar nova conta\n-Sair\n\n:')
        if consulta in ['jogar', 'Jogar', '1']:
            lista_usuários = ler_json()
            jogar_game(lista_usuários)
            time.sleep(2)
        elif consulta in ['consultar', 'Consultar', '2', 'consultar informações', 'Consultar informações']:
            lista_usuários = ler_json()
            imprimir_usuários(lista_usuários)
            time.sleep(2)
        elif consulta in ['modificar', 'Modificar', 'Modificar informações', 'modificar informações', '3']:
            lista_usuários = ler_json()
            modificar_informacoes(lista_usuários)
            time.sleep(2)
        elif consulta in ['Excluir', 'excluir', 'excluir conta', 'Excluir conta', '4']:
            lista_usuários = ler_json()
            excluir_conta(lista_usuários)
            time.sleep(2)
        elif consulta in ['Logar', 'logar', '5', 'Logar em outra conta', 'logar em outra conta']:
            lista_usuários = ler_json()
            logar(lista_usuários)
            time.sleep(2)
        elif consulta in ['Criar', 'criar', '6', 'Criar nova conta', 'criar nova conta']:
            subprocess.run(["python", "SingUp.py"])
            exit()
            time.sleep(2)
        elif consulta in ['sair', 'Sair', '7']:
            exit()
            time.sleep(2)
        else:
            print('\nValor invalido!')
            time.sleep(2)
menu()