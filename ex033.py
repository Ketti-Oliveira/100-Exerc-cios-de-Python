valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
valor3 = float(input('Terceiro valor: '))
#analisando qual é o menor valor, se for o valor1 vai mostrar na tela, se não for, ele será substituido
menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
#analisando qual é o maior valor, se for o valor1 vai mostrar na tela, se não for, ele será substituido
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3
print('O maior valor é {} e o menor é {}'.format(maior, menor))

#OBJETIVO
#FAÇA UM PROGRAMA QUE LEIA TRÊZ NÚMERO E MOSTRE QULA É O MAIOR E QUAL É O MENOR