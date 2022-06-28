cid = str(input('Em que cidade você nasceu? ')).strip()
                                            #.strip para eliminar os espaços desnecessários da frase
print(cid[:5].upper() == 'SANTO')
                        #a frase 'SANTO' tem que estar em maiúscula
        #[:5] para contar as 5 letras que há na palavra 'santo', se fosse 'sao' seria [:3]
        #.upper para colocar toda a palavra em maiúscula, assim evita de dar algum erro caso o
        #usuário digite letras maiúsculas, minúsculas etc, assim tod a frase vai para maiúscula
        #e o programa consegue ser executado normalmente


#OBJETIVO
#CRIE UM PROGRAMA QUE QUE LEIA O NOME DE UMA CIDADE E DIGA SE COMEÇA OU NÃO COM 'SANTO'