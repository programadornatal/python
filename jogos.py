import adivinhacaocomnivel
import forca


def escolhe_jogo():
    print('*****************************')
    print('***Escolha o seu jogo***')
    print('*****************************')

    print('(1) Adivinhação (2) Forca')
    jogo = int(input('Qual jogo? '))

    if jogo == 1:
        adivinhacaocomnivel.jogar()
    else:
        forca.jogar()


if (__name__ == '__main__'):
    escolhe_jogo()
