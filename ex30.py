num = int(input('Digite um número: '))
resultado = num % 2
    # '%' QUER DIZER MÓDULO QUE É O RESTO DE UMA DIVISÃO, SENDO ASSIM O RESTO DE
    # DE UMA DIVISÃO DE QUALQUER NÚMERO PAR POR 2 É 0
    #ASSIM COMO O RESTO DE UMA DIVISÃO DE QUALQUER NÚMERO ÍMPAR POR 2 É 1
if resultado == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))

#OBJETIVO:
#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE SE O NÚMERO
#É ÍMPAR OU PAR