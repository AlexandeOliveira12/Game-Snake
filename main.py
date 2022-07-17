# Importando bibliotecas
#from email import message_from_binary_file
import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Importando componentes do Jogo
from Components.Screen import *
from Components.CollisionParameters import *

pygame.init()

# Criando altura e largura
screen = pygame.display.set_mode((height, width))
print('A tela foi aberta')

# Mudando o nome da janela
pygame.display.set_caption(Name)

# Controlar o FPS
watch = pygame.time.Clock()

# Colocando o objeto no meio da tela
x = width/2
y = height/2

# Definindo Tipo do texto
font = pygame.font.SysFont('arial', 40, True, True)
pontos = 0

# Loop
while True:
    
    # Taxa de quadros por segundo (FPS)
    watch.tick(130)
    
    # Apagar a trajetoria do retangulo
    screen.fill((0,0,0))
    
    # Texto na tela
    message = f'Pontos: {pontos}'
    text = font.render(message, True, (255,255,255))
    for event in pygame.event.get(): 
        # Fechando a tela quando o quando o botão de fechar for pressionado
        if event.type == QUIT:
            pygame.quit()
            print('A tela foi fechada')
            exit()
   
   
    # Pressionando Teclas para se movimentar             
    if pygame.key.get_pressed()[K_a]:
        x = x - 4
    if pygame.key.get_pressed()[K_d]:
        x = x + 4
    if pygame.key.get_pressed()[K_w]:
        y = y - 4
    if pygame.key.get_pressed()[K_s]:
        y = y + 4                       
    
    #Retangulo Vermelho
    ret_vermelho = pygame.draw.rect(screen, (255,0,0), (x,y,40,50))
    
    # Retangulo Azul
    ret_azul = pygame.draw.rect(screen,(0,0,255), (x_azul,y_azul,40,50))
    
    #Colisão entre os retangulos
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
        
        
    screen.blit(text, (430,50))
    
    # Deixando a tela do jogo em loop
    pygame.display.update()  
                  
            