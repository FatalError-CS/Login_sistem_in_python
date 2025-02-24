import time

repetir = True
while repetir:
    input('\nBem-vindo ao jogo: encontre o Daniel, aperte enter para iniciar:')
    
    while True:
        escolha = input('Escolha uma arma: 1-espada; 2-arco; 3-chicote:')
        if escolha not in ["1", "2", "3", "12072024"]:
            print('Opção inválida!')
        else:
            break
    
    if escolha == "1":
        print("Você escolheu espada!")
    elif escolha == "2":
        print("Você escolheu arco!")
    elif escolha == "3":
        print("Você escolheu chicote!")
    elif escolha == "12072024":
        print("Você escolheu M4A4S!")
    
    h = True
    while h:
        x = input("Arma selecionada, pronto para aventura? s ou n:")
        if x not in ["s", "n", "não", "nao", "sim"]:
            print("Opção inválida")
        elif x == "n" or x == "não":
            print("Você desistiu!")
            repetir = False
            h = False
        elif x == "s" or x == "sim":
            input("Você é Jão, o melhor amigo de Daniel, mas Daniel está desaparecido...")
            input("Sua aventura começa no esgoto!")
            input("Capítulo 1: O início da busca.")
            input("Você ouve um barulho e decide investigar...")
            
            l = True
            while l:
                hpal = input("Há 3 caminhos: 1-esquerda; 2-frente; 3-direita:")
                if hpal not in ["1", "2", "3"]:
                    print('Opção inválida!')
                elif hpal == "1":
                    input("Você encontra Iudi, um amigo de Daniel, mas ele parece estranho!")
                    gg = True
                    while gg:
                        a1 = input("1-atacar; 2-defender-se; 3-fugir; 4-conversar:")
                        if a1 not in ["1", "2", "3", "4"]:
                            print('Opção inválida!')
                        elif a1 == "1" and escolha == "1":
                            input("Você ataca, mas Iudi te acerta em cheio!")
                        elif a1 == "2":
                            print("Você se defende, mas seu escudo quebra!")
                        elif a1 == "3":
                            input("Você tenta fugir, mas não consegue!")
                        elif a1 == "4":
                            input("Você tenta conversar com Iudi, mas ele não parece interessado...")
                elif hpal == "2":
                    input("Você segue em frente e encontra um barulho misterioso...")
                elif hpal == "3":
                    input("Você encontra o quadro de Daniel vestido de poni!")
                
                if hpal == "1" or hpal == "2" or hpal == "3":
                    break
            break
    
    # Verifica se o jogador quer jogar novamente após completar ou desistir
    if not repetir:
        y = input("Deseja jogar novamente? s ou n:")
        if y == "n" or y == "não":
            break
        elif y == "s" or y == "sim":
            repetir = True