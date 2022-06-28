from datetime import date   #para dentro da biblioteca datetime importar apenas a data
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year         #para buscar na data(date) de hoje(today) e mostrar apenas o ano(year)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é Bissexto!'.format(ano))
#OBJETIVO:
#FAÇA UM PROGRAMA QUE LEIA UM ANO E MOSTRE SE ELE É BISSXTO.