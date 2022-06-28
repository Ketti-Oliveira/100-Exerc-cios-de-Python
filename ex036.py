casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quanos você quer pagar? '))
parcela  = casa / (anos * 12)
print('Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}'.format(casa, anos, parcela))
if parcela <= salario * 30 / 100:
    print('Parábens! Empréstimo \033[1;30;44mAPROVADO\033[m!')
else:
    print('Desculpe! Empréstimo \033[1;30;41mRECUSADO\033[m!')
#OBJETIVO
#ESCREVA UM PROGRAMA PARA APROVAR UM EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. PERGUNTE O VALOR
#DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
#A PRESTAÇÃO MENSAL NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRESTIMO SERÁ NEGADO.