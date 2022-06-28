peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {} e você está abaixo do Peso!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f} e você está com o Peso Ideal!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f} e é considerado como Sobrepeso!'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f} e é considerado como Obesidade!'.format(imc))
else:
    print('Seu IMC é {:1f} e é considerado como Obesidade Mórbida!'.format(imc))
#OBJETIVO
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
# Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida