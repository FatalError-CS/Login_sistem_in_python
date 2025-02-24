import subprocess
import time
import json
import sys

def ler_valor_nao_vazio(usuário_variavel):
    valor_lido = input(f'\nEntre com o nome de {usuário_variavel}: ')
    while valor_lido == '':
        print(f'\nO nome de {usuário_variavel} não pode ser vazio!')
        valor_lido = input(f'\nEntre com o nome de {usuário_variavel}: ')
    return valor_lido

def ler_valor_de_senha(senha_variavel):
    valor_lido = input(f'\nEntre com a {senha_variavel} de usuário: ')
    while valor_lido == '':
        print(f'\nA {senha_variavel} não pode ser vazia!')
        valor_lido = input(f'\nEntre com a {senha_variavel} de usuário: ')
    return valor_lido

def carregar():
    pontos = ['.', '.', '.']
    for ponto in pontos:
        sys.stdout.write(ponto)
        sys.stdout.flush()
        time.sleep(1)

def verificar_login(lista_usuarios):
    usuario = ler_valor_nao_vazio('usuário')
    senha = ler_valor_de_senha('senha')
    for conta in lista_usuarios:
        if conta['usuário'] == usuario and conta['senha'] == senha:
            print('______________________________')
            print('\nLogin bem-sucedido!\n\nRedirecionando', end='')
            carregar()
            return True
    print('______________________________')
    print("\nErro: Nome de usuário ou senha incorretos!\n\nTente novamente")
    print('______________________________\n')
    return False
    
def ler_json():
    with open("contas.json", "r") as meu_arquivo:
        lista_usuarios = json.load(meu_arquivo)
    return lista_usuarios

def login():
    lista_usuarios = ler_json()
    while True:
        usuario_logado = verificar_login(lista_usuarios)
        if usuario_logado:
            subprocess.run(["python", "MenuPrincipal.py"])
            return usuario_logado

usuario_logado = login()