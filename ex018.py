import math
ang = float(input('Digite o ângulo que vc deseja? '))
sen = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
cos = math.cos((math.radians(ang)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))




#OBEJETIVO
#Faça um programa que leia um ângulo qualquer e mostre na tela o
#valor do seno cosseno e tangente desse angulo.