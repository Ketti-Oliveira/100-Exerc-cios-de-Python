nome = input('Digite seu nome completo: ').strip()
                                        #.strip é para os espaços antes e depois das palavras
                                        #que o usuário venha a digitar.
print('Analisando o seu nome...')
print('Seu nome em maíusculas é {}'.format(nome.upper()))
                                              #.upper para transformar tudo em maíuscula
print('Seu nome em minúsculas é {}'.format(nome.lower()))
                                              #.lower para colocar toda a frase em minúscula
print('seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
                                              #len para ler a quantidade de letras que há na
                                              #palavra frase digitada

                                              # - .count('  ') para tirar o que vc quer da frase
                                              #nesse caso o espaço do meio para somar apenas as letras
# 1° forma: print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
             #.split para criar uma lista com todas as frases digitadas
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

      #OBJETIVO:
#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
#   *O NOME COM TODAS AS LETRAS MAIÚSCULAS
#   *O NOME COM TODAS AS LETRAS MINÚSCULAS
#   *QUANTAS LETRAS TEM O NOME COMPLETO
#   *QUAL É O PRIMEIRO NOME E QUANTAS LETRAS TEM