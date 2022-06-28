preco = float(input('Qual o preço do produto? R$'))
desconto = preco*5/100
#Para calcular a porcentagem é necessário fazer o valor que quer ver o desconto ex: 1875,
#multiplicar ele pela a porcentagem que vc quer encontrar ex 5%, e depois dividir por 100
#sendo assim 1875x5=9.375, e depois 9.375/100=93.75, então 5% de desconto de 1875 é 93.75

print ('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preco, preco-desconto))

#OBJETIVO:
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.