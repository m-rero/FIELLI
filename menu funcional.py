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

altura_botao = 80
largura_botao = 330
fonteTitulo = pygame.font.Font('script/fontes/OMORI-GAME2.ttf', 260) #fonte do botao
fontegame = pygame.font.Font('script/fontes/Retro Gaming.ttf ', 60) #fonte do botao

textobotao1 = fontegame.render('START', True, 'white') #renderizar o botao na superficie
textobotao2 = fontegame.render('OPTIONS', True, 'white')
textobotao3 = fontegame.render('QUIT', True, 'white')
titulo = fonteTitulo.render('FIELLI', True, (255, 180, 24))

button1 = pygame.Rect(335, 320, largura_botao, altura_botao) #retangulo do botao posicao, posicao, tamanho largura, tamanho altura
borderbutton1 = pygame.Rect(330, 315, largura_botao + 10, altura_botao + 10) #da borda
button2 = pygame.Rect(335, 435, largura_botao, altura_botao)
borderbutton2 = pygame.Rect(330, 430, largura_botao + 10, altura_botao + 10)
button3 = pygame.Rect(335, 550, largura_botao, altura_botao)
borderbutton3 = pygame.Rect(330, 545, largura_botao + 10, altura_botao + 10)

bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img,(tela_largura, tela_comprimento))

while True:
    tela.blit(bg_img_resize, (0, 0))

    tela.blit(titulo, (250, 15)) #titulo

    for events in pygame.event.get(): #botao start
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN: #cursor em cima do botao
            if button1.collidepoint(events.pos): #cursor aperta o botao
                click.play()
                exec(open("main.py").read())
            if button2.collidepoint(events.pos): #cursor aperta o botao
                click.play()
                exec(open("creditos.py").read())
            if button3.collidepoint(events.pos): #cursor aperta o botao
                click.play()
                pygame.quit()

    a,b = pygame.mouse.get_pos()
    if button1.x <= a <= button1.x + largura_botao and button1.y <= b <= button1.y + altura_botao: #cursor em cima do botao
        pygame.draw.rect(tela, (255, 255, 255), borderbutton1)
        pygame.draw.rect(tela, (255, 157, 24), button1) #cor com mouse *
    else:
        pygame.draw.rect(tela, (255, 255, 255), borderbutton1)
        pygame.draw.rect(tela, (242, 106, 24), button1) #cor sem mouse default *
    tela.blit(textobotao1, (button1.x + 47, button1.y + 2)) #borda do botao

    c,d = pygame.mouse.get_pos()
    if button2.x <= c <= button2.x + largura_botao and button2.y <= d <= button2.y + altura_botao: #cursor em cima do botao
        pygame.draw.rect(tela, (255, 255, 255), borderbutton2)
        pygame.draw.rect(tela, (255, 157, 24), button2) #cor com mouse *
    else:
        pygame.draw.rect(tela, (255, 255, 255), borderbutton2)
        pygame.draw.rect(tela, (242, 106, 24), button2) #cor sem mouse default *
    tela.blit(textobotao2, (button2.x + 6, button2.y + 2)) #borda do botao

    e,f = pygame.mouse.get_pos()
    if button3.x <= e <= button3.x + largura_botao and button3.y <= f <= button3.y + altura_botao: #cursor em cima do botao
        pygame.draw.rect(tela, (255, 255, 255), borderbutton3)
        pygame.draw.rect(tela, (255, 157, 24), button3) #cor com mouse *
    else:
        pygame.draw.rect(tela, (255, 255, 255), borderbutton3)
        pygame.draw.rect(tela, (242, 106, 24), button3) #cor sem mouse default *
    tela.blit(textobotao3, (button3.x + 75, button3.y + 2)) #borda do botao

    pygame.display.update()
