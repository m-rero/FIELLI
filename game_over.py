
import pygame
pygame.init() #inicia todos os modulos instalados de pygame

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
pygame.display.set_caption('MENU') #legenda da tela

#som
click = pygame.mixer.Sound('sons/click.mp3')
pygame.mixer.init()
pygame.mixer.music.load('sons/death.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

altura_botao = 75
largura_botao = 500
fonteTitulo = pygame.font.Font('script/fontes/OMORI-GAME2.ttf', 195) #fonte do botao
fontegame = pygame.font.Font('script/fontes/Retro Gaming.ttf ', 60) #fonte do botao

textobotao1 = fontegame.render('TRY AGAIN', True, 'white') #renderizar o botao na superficie
textobotao2 = fontegame.render('MENU', True, 'white')
titulo = fonteTitulo.render('GAME OVER', True, (232, 5, 5))

button1 = pygame.Rect(250, 300, largura_botao, altura_botao) #retangulo do botao posicao, posicao, tamanho largura, tamanho altura
borderbutton1 = pygame.Rect(245, 295, largura_botao + 10, altura_botao + 10) #da borda
button2 = pygame.Rect(250, 420, largura_botao, altura_botao)
borderbutton2 = pygame.Rect(245, 415, largura_botao + 10, altura_botao + 10)

bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img,(tela_largura, tela_comprimento))

while True:
    tela.blit(bg_img_resize, (0, 0))

    tela.blit(titulo, (137, 30)) #titulo

    for events in pygame.event.get(): #botao start
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN: #cursor em cima do botao
            if button1.collidepoint(events.pos): #cursor aperta o botao
                click.play()
                exec(open("main.py").read())
            if button2.collidepoint(events.pos): #cursor aperta o botao
                click.play()
                exec(open("FIELLI.py").read())

    a,b = pygame.mouse.get_pos()
    if button1.x <= a <= button1.x + largura_botao and button1.y <= b <= button1.y + altura_botao: #cursor em cima do botao
        pygame.draw.rect(tela, (255, 255, 255), borderbutton1)
        pygame.draw.rect(tela, (74, 7, 7), button1) #cor com mouse *
    else:
        pygame.draw.rect(tela, (255, 255, 255), borderbutton1)
        pygame.draw.rect(tela, (145, 10, 10), button1) #cor sem mouse default *
    tela.blit(textobotao1, (button1.x + 44, button1.y + 2)) #borda do botao

    c,d = pygame.mouse.get_pos()
    if button2.x <= c <= button2.x + largura_botao and button2.y <= d <= button2.y + altura_botao: #cursor em cima do botao
        pygame.draw.rect(tela, (255, 255, 255), borderbutton2)
        pygame.draw.rect(tela, (74, 7, 7), button2) #cor com mouse *
    else:
        pygame.draw.rect(tela, (255, 255, 255), borderbutton2)
        pygame.draw.rect(tela, (145, 10, 10), button2) #cor sem mouse default *
    tela.blit(textobotao2, (button2.x + 150, button2.y + 2)) #borda do botao


    pygame.display.update()
    
# Música Para
pygame.mixer.music.stop()
pygame.mixer.quit()
