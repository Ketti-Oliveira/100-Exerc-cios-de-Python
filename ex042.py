r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É POSSÍVEL formar um triângulo!')
    if r1 == r2 and r2 == r3:
        print('É um triângulo EQUILÁTERO')
    elif r1 != r2 and r1 != r3 and r2 != r1 and r2 != r3 and r3 != r2 and r3 != r1:
        print('É um triângulo ESCALENO')
    else:
        print('É um triângulo ISÓSCELES!')
else:
    print('NÃO É POSSÍVEL formar um Triângulo!')
#OBJETIVO:
#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes