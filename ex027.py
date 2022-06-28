n = str(input('Digite o seu nome completo: ')).strip().upper()
nome = n.split()
        #.split vai fatiar a string, separando cada palavra da frase
        #e assim criando uma lista
print('Prazer em te conhecer!')
print('Seu primeiro nome  é {}'.format(nome[0]))
print('Seu último nome é {} '.format(nome[len(nome)-1]))

#BJETIVO
#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA,
#MOSTRANDO EM SEGUIDA O PRIMEIRO E ÚLTIMO NOME SEPARADAMENTE.