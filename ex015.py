dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor = dias*60 + km*0.15
print('O total a pagar é de R${:.2f}'.format(valor))

#OBJETIVO
#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a...
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que...
#o carros custa R$60 por dia e R$0,15 por km rodado.