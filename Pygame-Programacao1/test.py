import pygame
from pygame.locals import *

#init
pygame.init()

#tela do jogo
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('FIELLI')

# definição do icone do executável
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#music begin
pygame.mixer.init()
pygame.mixer.music.load('sons/intro.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
#som
pulo = pygame.mixer.Sound('sons/cat.mp3')
click = pygame.mixer.Sound('sons/click.mp3')
pegar = pygame.mixer.Sound('sons/pick.mp3')


clock = pygame.time.Clock()
fps= 60

#images
bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img, (screen_width, screen_height))
bloco = pygame.image.load('img/bloco2.png')
rocha = pygame.image.load('img/bloco.png')
plataforma = pygame.image.load('img/plaforma.jpg')
ouro_img = pygame.image.load('img/ouro.png')
fogo = pygame.image.load('img/fogo.png')
salvar = pygame.image.load('img/save.png')
carregar = pygame.image.load('img/load.png')
peca = pygame.image.load('img/peca1.png')
peca_x = 500
peca_y = 200

######################################################################

#Carregue a imagem do jogador
jogador_img = pygame.image.load('img/gato/spritesfielli/1.png')
jogador_x = 0  # Posição inicial do jogador no eixo X
jogador_y = 0  # Posição inicial do jogador no eixo Y
jogador_velocidade = 5  # Velocidade de movimento do jogador
pulando = False  # Flag para controlar o pulo
salto = 10  # Força do salto
gravidade = 1  # Força da gravidade

# Carregue a imagem do obstáculo
obstaculo_img = pygame.image.load('img/bloco.png')
obstaculo_width = obstaculo_img.get_width()  # Largura do obstáculo
obstaculo_height = obstaculo_img.get_height()  # Altura do obstáculo
obstaculo_x = (screen_width - obstaculo_width) // 2  # Posição inicial do obstáculo no eixo X (centro da tela)
obstaculo_y = 0 # Posição inicial do obstáculo no eixo Y (topo da tela)


#######################################################################

#barra de pontuacao
pontuacao = 0
font = pygame.font.Font(None, 36) 

##########################################################################

#game loop
run = True
while run:
    
    #image
    screen.blit(bg_img_resize, (0,0))
    
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
##############################################################################
         
         
         
    #pontuacao
    pygame.draw.rect(screen, (255, 255, 255), (680, 20, 100, 22))    
    
    # Renderizar o texto da pontuação
    texto_pontuacao = font.render('peças: ' + str(pontuacao), False, (0, 0, 0))
    screen.blit(texto_pontuacao, (683, 20)) 
    
    # colisao jogador e peca
    jogador_rect = pygame.Rect(jogador_x, jogador_y, jogador_img.get_width(), jogador_img.get_height())
    peca_rect = pygame.Rect(peca_x, peca_y, peca.get_width(), peca.get_height())

    if jogador_rect.colliderect(peca_rect):
        pontuacao += 1
        click.play()
        peca_x = -peca.get_width() 
        peca_y = -peca.get_height()  
    else:
        screen.blit(peca, (peca_x, peca_y))
        
    
##############################################################################   
  
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
        
     # Lógica de pulo
    if not pulando and teclas[pygame.K_SPACE]:  # Pressionar a barra de espaço para pular
        pulando = True
        pulo.play()

        
    if pulando:
        jogador_y -= salto
        salto -= gravidade
        if salto <= -10:  # Defina a altura máxima do salto
            pulando = False
            salto = 10
    
    # Aplicar a gravidade
    if not pulando:
        jogador_y += gravidade
        
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
    screen.blit(obstaculo_img, (obstaculo_x, obstaculo_y))
    screen.blit(peca, (peca_x, peca_y))

######################################################################### 
    pygame.display.update()
    
    clock.tick(fps)
    

#music stop
pygame.mixer.music.stop()
pygame.mixer.quit()   

#quit
pygame.quit()
