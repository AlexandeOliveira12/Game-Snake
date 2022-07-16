# Importando bibliotecas
from turtle import width
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Criando altura e largura
height = 640
width = 480

screen = pygame.display.set_mode((height, width))
print('A tela foi aberta')

#Mudando o nome da janela
pygame.display.set_caption('Tela do jogo')

#Criando loop
while True:
    for event in pygame.event.get():
        
        #Fechando a tela quando o quando o botão de fechar for pressionado
        if event.type == QUIT:
            pygame.quit()
            print('A tela foi fechada')
            exit()
    
    #Desenhando figuras, parametros (onde vai ser apresentado(tela), cor(RGB); 
    #Para figuras sem Raio(posição X, posição Y, Largura e Altura), Para figuras com Raio (Posição X, Posição Y e Raio));
    pygame.draw.rect(screen, (255,0,0), (200,300,40,50))
    pygame.draw.circle(screen, (0,200,0), (300,260), 40)
        
    #Deixando a tela do jogo em loop
    pygame.display.update()  
                  
            