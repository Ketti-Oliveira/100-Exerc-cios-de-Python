vel = float(input('Qual a velocidade atual do veículo? '))
if vel >= 80:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h ')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
    print('Tenha um bom dia! Dirija com segurança.')
else:
    print('Tenha um bom dia! Dirija com segurança.')
#OBJETIVO:
#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80KM/H,
#MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO. A MULTA VAI CUSTAR 7,00 POR KM ACIMA DO LIMITE