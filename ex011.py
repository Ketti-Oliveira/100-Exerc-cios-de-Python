lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar*alt
print('Sua parede tem {}x{} e sua área é de {}m².'.format(lar, alt, lar*alt))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(area/2))


#OBJETIVO:
#Crie um programa que leia a largura e a altura de uma parede em metros...
#calcule a sua área e a quantidade de tintas para pintá-la, sabendo...
#que cada litro de tinta pinta uma área de 2 metros quadrados