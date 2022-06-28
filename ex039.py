from datetime import date
nasc = int(input('Em que ano você nasceu? '))
ano = date.today().year
idade = (ano - nasc)
print('Sua idade é {}'.format(idade))
if idade > 18:
    print('De acordo com sua idade, faz {} anos que \033[1;30;41mPASSOU O PRAZO\033[m do seu alistamento!'.format(idade - 18))
elif idade < 18:
    print('De acordo com sua idade, \033[1;30;44mFALTA {} anos\033[m, para você poder se alistar!'.format(18 - idade))
else:
    print('Está no momento \033[1;30;42mEXATO\033[m para você se alistar!')
#OBJETIVO
#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM  SUA IDADE
#SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR, SE É A HORA EXATA DE SE ALISTAR OU SE JÁ PASSOU DO
#TEMPO DE ALISTAMENTO. SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.