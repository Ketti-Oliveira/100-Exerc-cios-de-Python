num = int(input('Digite um número: '))
opcao = int(input('{}\n'
                 '{}Escolha uma opção:\n'
                 '1- Conversão para BINÁRIO\n'
                 '2- Conversão para OCTAL\n'
                 '3- Conversão para HEXADECIMAL\n'
                 '>> '.format(15 * '-=', 4 * ' ')))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) #[2:] é para começar a partir
                                                                                # da terceira letra da string
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')

#OBJETIVO:
#ESCREVA UM PROGRAMA EM PYTHON QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER
#QUAL SERÁ A BASE DE CONVERSÃO: 1 PARA BINÁRIO, 2 PARA OCTAL E 3 PARA HEXADECIMAL
