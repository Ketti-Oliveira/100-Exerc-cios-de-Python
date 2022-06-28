salario = float(input('Qual é o seu salário R$? '))
if salario <= 1250:
    valor = salario * 15 /100 + salario
    porcentagem = '15%'
else:
    valor = salario * 10 / 100 + salario
    porcentagem = '10%'
print('O seu salário era R${:.2f}, com o aumento de {}, passou a ser R${:.2f}'.format(salario, porcentagem, valor))

#OBJETIVO
#ESCREVA UM RPOGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMNETO.
#PARA SALÁRIOS SUPERIORES A 1250, CALCULE UM AUMENTO DE 10%. PARA SALÁRIOS INFERIORES OU IGUAIS, O AUMENTO É DE 15%