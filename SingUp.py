import subprocess
import time
import sys
import json
from datetime import datetime

def ler_valor_nao_vazio(usuário_variavel):
    valor_lido = input(f'\nCrie um nome de {usuário_variavel}: ')
    while valor_lido == '':
        print(f'\nO nome de {usuário_variavel} não pode ser vazio!')
        valor_lido = input(f'Crie um nome de {usuário_variavel}: ')
    return valor_lido

def ler_valor_de_senha(senha_variavel):
    valor_lido = input(f'\nCrie uma {senha_variavel} para o usuário: ')
    while valor_lido == '':
        print(f'\nA {senha_variavel} não pode ser vazia!')
        valor_lido = input(f'Crie uma {senha_variavel} para o usuário: ')
    return valor_lido

def verifica_data_valida(data_texto):
    try:
        data_valida = datetime.strptime(data_texto, "%d/%m/%Y")
        return True
    except:
        return False

def ler_data_valida():
    dataNascimentoString = input('\nEntre com a data de nascimento: ')
    while not verifica_data_valida(dataNascimentoString):
        print('\nData inválida!')
        dataNascimentoString = input('Entre com a data de nascimento: ')
    dataNascimento = datetime.strptime(dataNascimentoString, "%d/%m/%Y")
    print()
    return dataNascimento

def carregar():
    pontos = ['.', '.', '.']
    for ponto in pontos:
        sys.stdout.write(ponto)
        sys.stdout.flush()
        time.sleep(1)

def ler_Conta(lista_usuarios):
    while True:
        usuário = ler_valor_nao_vazio('usuário')
        if verificar_usuario_existe(usuário, lista_usuarios):
            print("\nErro: Este nome de usuário já está em uso. Por favor, escolha outro.\n")
        else:
            break
    senha = ler_valor_de_senha('senha')
    dataNascimento = ler_data_valida()
    Conta = {
        'usuário': usuário,
        'senha': senha,
        'dataNascimento': dataNascimento.strftime('%d/%m/%Y'),
    }
    print('______________________________')
    print('\nConta criada!\n\nRedirecionando', end='')
    carregar()
    return Conta

def verificar_usuario_existe(usuario, lista_usuarios):
    for conta in lista_usuarios:
        if conta['usuário'] == usuario:
            return True
    return False


def ler_json():
    with open("contas.json", "r") as meu_arquivo:
        lista_usuários = json.load(meu_arquivo)
    return lista_usuários

def salvar_json(lista):
    with open("contas.json", "w") as meu_arquivo:
        lista_json = json.dumps(lista_usuários, indent=4)
        meu_arquivo.write(lista_json)

lista_usuários = ler_json()

for i in range(1):
    meu_usuário = ler_Conta(lista_usuários)
    lista_usuários.append(meu_usuário)
    salvar_json(lista_usuários)
    subprocess.run(["python", "MenuPrincipal.py"])
    exit()