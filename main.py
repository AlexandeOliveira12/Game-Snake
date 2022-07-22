# Importando bibliotecas
import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Importando componentes do Jogo
from Components.Screen import *
from Components.CollisionParameters import *

pygame.init()

# Importando Musicas
# Musica de fundo
background_noise = pygame.mixer.music.load('./Sounds/CatSound.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

# Musica de Colisão
noise_collision = pygame.mixer.Sound('./Sounds/SoundCoin.wav')

# Altura e largura
screen = pygame.display.set_mode((height, width))
print('A tela foi aberta')

# Nome da janela
pygame.display.set_caption(Name)

# Controlar o FPS
watch = pygame.time.Clock()

# Centralizando objeto
x_snake = int(width/2)
y_snake = int(height/2)

# Tipo do texto
font = pygame.font.SysFont('arial', 40, True, True)
    
# Loop
while True:
    
    # Taxa de quadros por segundos
    watch.tick(120)
    
    # Apagar a trajetoria
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
            x_snake = x_snake - 15
        if pygame.key.get_pressed()[K_d]:
            x_snake = x_snake + 15
        if pygame.key.get_pressed()[K_w]:
            y_snake = y_snake - 15
        if pygame.key.get_pressed()[K_s]:
            y_snake = y_snake + 15
    
    # Snake
    snake = pygame.draw.rect(screen, (0,255,0), (x_snake,y_snake,40,50))
    
    # Apple
    apple = pygame.draw.rect(screen,(255,0,0), (x_apple,y_apple,40,50))
    
    # Colisão
    if snake.colliderect(apple):
         x_apple = randint(40, 600)
         y_apple = randint(50, 430)
         pontos = pontos + 1
         noise_collision.play()
        
    screen.blit(text, (410,10))
    
    # Tela em loop
    pygame.display.update()  