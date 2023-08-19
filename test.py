import pygame
from pygame.locals import *

#init
pygame.init()

#tela do jogo
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#music begin
pygame.mixer.init()
pygame.mixer.music.load('game_sounds/intro.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
fps= 60

#images
bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img, (screen_width, screen_height))
bloco = pygame.image.load('img/bloco2.png')
rocha = pygame.image.load('img/bloco.png')
plataforma = pygame.image.load('img/plaforma.jpg')
ouro = pygame.image.load('img/ouro.png')
fogo = pygame.image.load('img/fogo.png')
salvar = pygame.image.load('img/save.png')
carregar = pygame.image.load('img/load.png')


######################################################################

#Carregue a imagem do jogador
jogador_img = pygame.image.load('img/gato/fiellibase1.png')
jogador_x = 0  # Posição inicial do jogador no eixo X
jogador_y = 0  # Posição inicial do jogador no eixo Y
jogador_velocidade = 5  # Velocidade de movimento do jogador

#######################################################################

#game loop
run = True
while run:
    
    #image
    screen.blit(bg_img, (0,0))
    
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
########################################################################    
  
    # Captura as teclas pressionadas
    teclas = pygame.key.get_pressed()
    
    # Move o gato com base nas teclas pressionadas
    if teclas[pygame.K_LEFT]:
        jogador_x -= jogador_velocidade
    if teclas[pygame.K_RIGHT]:
        jogador_x += jogador_velocidade
    if teclas[pygame.K_UP]:
        jogador_y -= jogador_velocidade
    if teclas[pygame.K_DOWN]:
        jogador_y += jogador_velocidade
    
    # Verifique os limites horizontais
    if jogador_x < 0:
        jogador_x = 0
    elif jogador_x > screen_width - jogador_img.get_width():
        jogador_x = screen_width - jogador_img.get_width()
    
    # Verifique os limites verticais
    if jogador_y < 0:
        jogador_y = 0
    elif jogador_y > screen_height - jogador_img.get_height():
        jogador_y = screen_height - jogador_img.get_height()
   
   
    #image
    screen.blit(bg_img, (0, 0))
    
    # Desenhe o jogador na posição atual
    screen.blit(jogador_img, (jogador_x, jogador_y))

######################################################################### 
    pygame.display.update()
    
    clock.tick(fps)
   
#music stop
pygame.mixer.music.stop()
pygame.mixer.quit()   
            
#quit
pygame.quit()
