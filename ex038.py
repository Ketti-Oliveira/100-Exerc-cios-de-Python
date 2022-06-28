num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O \033[1;30;44mPRIMEIRO\033[m número é maior!')
elif num2 > num1:
    print('O \033[1;30;42mSEGUNDO\033[m número é maior!')
else:
    print('\033[1;30;41mNão existe valor maior! Os dois são iguais.\033[m')
#OBJETIVO
#ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS.
#MOSTRANDI NA TELA:
# - O PRIMEIRO NÚMERO É MAIOR
# - O SEGUNDO NÚMERO É MAIOR
# - NÃO EXISTE VALOR MAIOR OS DOIS SÃO IGUAIS