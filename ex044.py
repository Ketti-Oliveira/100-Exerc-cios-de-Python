valor = float(input('Digite o valor do Produto: R$ '))
pag = int(input('''Qual a forma de pagamento?
1- Dinheiro\n2- Cheque\n3- Cartão a vista\n4- 2X no cartão\n5- 3X ou mais no cartão.\n>> '''))
if pag == 1 or pag == 2:
    total = valor - (valor * 10 / 100)
elif pag == 3:
    total = valor - (valor * 5 / 100)
elif pag == 4:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif pag == 5:
    total = valor + (valor * 20 / 100)
    vezes = int(input('Em quantas vezes vai parcelar: '))
    parcela = total / vezes
    print('Sua compra será parcelada em {} vezes de R${:.2f} COM JUROS'.format(vezes, parcela))
else:
    total = valor
    print('\033[1;30;41mOPÇÃO INVÁLIDA! TENTE NOVAMENTE.\033[m')
print('Sua compra com valor de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
#OBJETIVO
#Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

