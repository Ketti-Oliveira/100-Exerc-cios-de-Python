frase = str(input('Digite uma frase: ')).upper().strip()
                                    #.upper para colocar afrase tod em maiúscula para caso o usuário
                                    #digite em minúscula o programa não apresentar erros

                                    #.strip() para eliminar os espaços indesejados caso o usuário digite
                                    #incorretamente, somente os espaços antes e depois da frase
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
                                            #.count() para contar quantas letras "A" tem na frase
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
                                            #.find para informar onde está a primeira letra "A"
                                            #a partir do lado esquerdo, +1 para contar a partir do número 1
                                            #pois na linguagem python conta a partir do 0
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))
                                            #.rfind para contar a primeira letra "A" a partir do lado direito
                                            #no caso a última letra "A" da frase

#OBJETIVO
#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE QUANTAS VEZES APARECE A LETRA
# "A", EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ E EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ.