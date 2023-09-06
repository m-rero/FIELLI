import pygame
pygame.init() #inicia todos os modulos instalados de pygame

screen = pygame.display.set_mode((1000, 700)) #cria a tela *
pygame.display.set_caption('MENU') #legenda da tela

#tela do jogo e configurações
tile_size = 50
cols = 20
margin = 100
tela_largura = tile_size * cols
tela_comprimento = (tile_size * cols) - 400 + margin
tela = pygame.display.set_mode((tela_largura, tela_comprimento))


altura_botao = 80
largura_botao = 330
fontegame = pygame.font.Font('script/fontes/Retro Gaming.ttf ', 60) #fonte do botao
#textobotao1 = fontegame.render('START', True, 'white') #renderizar o botao na superficie
textobotao2 = fontegame.render('OPTIONS', True, 'white')
textobotao3 = fontegame.render('QUIT', True, 'white')
#button1 = pygame.Rect(335, 500, largura_botao, altura_botao) #retangulo do botao posicao, posicao, tamanho largura, tamanho altura
#borderbutton1 = pygame.Rect(330, 495, largura_botao + 10, altura_botao + 10) #da borda
button2 = pygame.Rect(335, 435, largura_botao, altura_botao)
borderbutton2 = pygame.Rect(330, 430, largura_botao + 10, altura_botao + 10)
button3 = pygame.Rect(335, 550, largura_botao, altura_botao)
borderbutton3 = pygame.Rect(330, 545, largura_botao + 10, altura_botao + 10)
bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img,(tela_largura, tela_comprimento))

while True:
    screen.blit(bg_img_resize, (0, 0))

    for events in pygame.event.get(): #botao options
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN: #cursor em cima do botao
            if button2.collidepoint(events.pos): #cursor aperta o botao
                pygame.quit()
    a,b = pygame.mouse.get_pos()
    if button2.x <= a <= button2.x + largura_botao and button2.y <= b <= button2.y + altura_botao: #cursor em cima do botao
        pygame.draw.rect(screen, (255, 255, 255), borderbutton2)
        pygame.draw.rect(screen, (255, 157, 24), button2) #cor com mouse *
    else:
        pygame.draw.rect(screen, (255, 255, 255), borderbutton2)
        pygame.draw.rect(screen, (242, 106, 24), button2) #cor sem mouse default *
    screen.blit(textobotao2, (button2.x + 30, button2.y - 5)) #borda do botao


    for events in pygame.event.get(): #botao quit
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN: #cursor em cima do botao
            if button3.collidepoint(events.pos): #cursor aperta o botao
                pygame.quit()
    a,b = pygame.mouse.get_pos()
    if button3.x <= a <= button3.x + largura_botao and button3.y <= b <= button3.y + altura_botao: #cursor em cima do botao
        pygame.draw.rect(screen, (255, 255, 255), borderbutton3)
        pygame.draw.rect(screen, (255, 157, 24), button3) #cor com mouse *
    else:
        pygame.draw.rect(screen, (255, 255, 255), borderbutton3)
        pygame.draw.rect(screen, (242, 106, 24), button3) #cor sem mouse default *
    screen.blit(textobotao3, (button3.x + 65, button3.y - 5)) #borda do botao

    pygame.display.update()
