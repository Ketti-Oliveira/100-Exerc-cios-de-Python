import pygame
pygame.init()           #serve para iniciar a biblioteca do pygame
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()        #para iniciar a música
pygame.event.wait()         #para esperar tocar até o final


#OBJETIVO:
#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.