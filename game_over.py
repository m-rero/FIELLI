
import pygame
pygame.init() #inicia todos os modulos instalados de pygame

screen = pygame.display.set_mode((1000, 700)) #cria a tela *
pygame.display.set_caption('GAME OVER') #legenda da tela

#icone do executável
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#tela do jogo e configurações
tile_size = 50
cols = 20
margin = 100
tela_largura = tile_size * cols
tela_comprimento = (tile_size * cols) - 400 + margin
tela = pygame.display.set_mode((tela_largura, tela_comprimento))

#som
morte = pygame.mixer.Sound('sons/result.mp3')
click = pygame.mixer.Sound('sons/click.mp3')

altura_botao = 80
largura_botao = 500
fonteTitulo = pygame.font.Font('script/fontes/OMORI-GAME2.ttf', 175) #fonte do botao
fontegame = pygame.font.Font('script/fontes/Retro Gaming.ttf ', 65) #fonte do botao

textobotao1 = fontegame.render('TRY AGAIN', True, 'white') #renderizar o botao na superficie
titulo = fonteTitulo.render('GAMER OVER', True, (232, 5, 5))

button1 = pygame.Rect(250, 380, largura_botao, altura_botao) #retangulo do botao posicao, posicao, tamanho largura, tamanho altura
borderbutton1 = pygame.Rect(245, 375, largura_botao + 10, altura_botao + 10) #da borda

bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img,(tela_largura, tela_comprimento))

while True:
    screen.blit(bg_img_resize, (0, 0))

    screen.blit(titulo, (150, 100)) #titulo

    for events in pygame.event.get(): #botao start
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN: #cursor em cima do botao
            if button1.collidepoint(events.pos): #cursor aperta o botao
                click.play()
                #exec(open("main.py").read())
                pygame.quit()
    a,b = pygame.mouse.get_pos()
    if button1.x <= a <= button1.x + largura_botao and button1.y <= b <= button1.y + altura_botao: #cursor em cima do botao
        pygame.draw.rect(screen, (255, 255, 255), borderbutton1)
        pygame.draw.rect(screen, (74, 7, 7), button1) #cor com mouse *
    else:
        pygame.draw.rect(screen, (255, 255, 255), borderbutton1)
        pygame.draw.rect(screen, (145, 10, 10), button1) #cor sem mouse default *
    screen.blit(textobotao1, (button1.x + 39, button1.y + 2)) #borda do botao

    
    pygame.display.update()