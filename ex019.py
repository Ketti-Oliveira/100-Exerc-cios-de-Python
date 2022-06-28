from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)       #o comando choice é para escolher algum item da lista de forma aleatória
print('O aluno(a) escolhido foi {}'.format(escolhido))

#OBJETIVO
#Um professor quer sortear um dos alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.