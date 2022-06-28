prim = float(input('Digite a primeira nota do(a) aluno(a): '))
segun = float(input('Digite a segunda nota do(a) aluno(a): '))
media = (prim + segun) / 2
if media < 5.0:
    print('Sua média foi {:.1f}, infelizmente você foi \033[1;30;41mREPROVADO\033[m!'.format(media))
elif 5.0 <= media <= 6.9:
    print('Sua média foi {:.1f}, você está em \033[1;30;43mRECUPERAÇÃO\033[m!'.format(media))
else:
    print('Sua média foi {:.1f}, \033[1;30;42mPARABÉNS VOCÊ FOI APROVADO\033[m!'.format(media))
#OBJETIVO
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
#mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO