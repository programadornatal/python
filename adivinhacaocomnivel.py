import random

def jogar():
    print('*****************************')
    print('Bem vindo ao jogo da adivinhação')
    print('*****************************')

    #int arredonda para baixo, round arredonda para cima
    #numero_secreto = int(random.random() * 100)
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 100
    #rodada = 1

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        total_de_tentativas = 10
        pontos_perdidos = 10
    elif nivel == 2:
        total_de_tentativas = 5
        pontos_perdidos = 20
    else:
        total_de_tentativas = 3
        pontos_perdidos = 35

    for rodada in range(1, total_de_tentativas + 1):
        #print('Tentativa:', rodada, 'de', total_de_tentativas)
        print('Tentativa: {} de {}'.format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Você acertou o número secreto e fez {} pontos!'.format(pontos))
            break
        else:
            if maior:
                print("O chute foi maior do que o número secreto")
            #elif menor:
            else:
                print("O chute foi menor do que o número secreto")
            #pontos_perdidos = abs(numero_secreto - chute) #40-20 = 20 pontos perdidos
            pontos = pontos - pontos_perdidos
        if total_de_tentativas == rodada:
            print('########################', 'O número secreto é:', numero_secreto)
        #rodada = rodada + 1
    print('Fim do jogo')
if(__name__ == '__main__'):
    jogar()