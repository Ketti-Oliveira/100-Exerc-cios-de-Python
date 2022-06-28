from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Qual o ano de nascimento do atleta? '))
idade = anoAtual - anoNasc
print('O atleta que nasceu em {}, tem {} anos.'.format(anoNasc, idade))
if idade <= 9:
    print('É considerado Atleta \033[1;30;41mMIRIM\033[m!')
elif 9 < idade <= 14:
    print('É considerado Atleta \033[1;30;43mINFANTIL\033[m!')
elif 14 < idade <= 19:
    print('É considerado Atleta \033[1;30;44mJÚNIOR\033[m!')
elif 19 < idade <= 25:
    print('É considerado Atleta \033[1;30;42mSÊNIOR\033[m!')
else:
    print('é considerado \033[7;30;42mAtleta MASTER\033[m!')


#OBJETIVO
#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

