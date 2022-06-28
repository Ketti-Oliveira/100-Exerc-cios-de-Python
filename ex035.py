print('-='*20)
print(8*' ', 'Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos a cima PODEM FORMAR Triângulo!')
else:
    print('Os seguimentos a cima NÃO PODEM FORMAR Triângulo!')

#OBJETIVO
#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM
#OU NÃO FORMAR UM TRIÂNGULO