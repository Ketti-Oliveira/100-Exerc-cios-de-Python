from random import randint      #ESTE MÓDULO É PARA SORTEAR ALGO
from time import sleep          #ESTE MÓDULO É PARA CONTAR OS SEGUNDOS, CONTABILIAR OS SEGUNDO
                                #ANTES DE ALGUMA AÇÃO
itens =('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('JOOH')
sleep(1)                        #para demorar um segundo antes de execuatar a próxima ação
print('KEEN')
sleep(1)                        #para demorar um segundo antes de execuatar a próxima ação
print('PÔÔH!!!')
print(12*'-=')
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print(12*'-=')
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('\033[1;30;43mEMPATE!!!\033[m')
    elif jogador == 1:
        print('\033[1;30;44mO JOGADOR VENCEU!!!\033[m')
    elif jogador == 2:
        print('\033[1;30;42mO COMPUTADOR VENCEU!!!\033[m')
    else:
        print('\033[1;30;41mJOGADA INVÁLIDA!!!\033[m')
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('\033[1;30;42mO COMPUTADOR VENCEU!!!\033[m')
    elif jogador == 1:
        print('\033[1;30;43mEMPATE!!!\033[m')
    elif jogador == 2:
        print('\033[1;30;44mO JOGADOR VENCEU!!!\033[m')
    else:
        print('\033[1;30;41mJOGADA INVÁLIDA!!!\033[m')
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('\033[1;30;44mO JOGADOR VENCEU!!!\033[m')
    elif jogador == 1:
        print('\033[1;30;42mO COMPUTADOR VENCEU!!!\033[m')
    elif jogador == 2:
        print('\033[1;30;43mEMPATE!!!\033[m')
    else:
        print('\033[1;30;41mJOGADA INVÁLIDA!!!\033[m')
else:
    print('\033[1;30;41mJOGADA INVÁLIDA!!!\033[m')
#OBJETIVO:
#Crie um programa que faça o computador jogar Jokenpô com você.
