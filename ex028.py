from random import randint      #importar o módulo random
from time import sleep          # importar a biblioteca sleep, usando apenas o time para contar os segundos
comp = randint(0, 5)    #RANDINT() FAZ O COMPUTAR "PENSAR" OU SORTEAR O QUE FOR SOLICITADO
                        # NESSE CASO UM NÚMERO ENTRE 0 E 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ? '))
print('Processando...')
sleep(4)
if jogador == comp:
    print('Parabéns você venceu!')
else:
    print('ERROU, EU GANHEI! HAHAHAHHAAH')
    print('Eu pensei no número {} e não no {}'.format(comp, jogador))
print('-=-' * 20)

#OBJETIVO
#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR 'PENSAR' EM UM NÚMERO DE
#0 A 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO
#PELO COMPUTADOR. O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU