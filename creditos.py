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
pygame.display.set_caption('CREDITS') #legenda da tela

#som
click = pygame.mixer.Sound('sons/click.mp3')

altura_botao = 80
largura_botao = 330
fonteTitulo = pygame.font.Font('script/fontes/OMORI-GAME2.ttf', 170) 
fonteNomes = pygame.font.Font('script/fontes/OMORI-GAME2.ttf', 40) 
fontegame = pygame.font.Font('script/fontes/Retro Gaming.ttf ', 60) #fonte do botao

textoBotaoBack = fontegame.render('BACK', True, 'white') #renderizar o botao na superficie
tituloCreditos = fonteTitulo.render('CREDITS', True, (255, 180, 24))
nome1 = fonteNomes.render('Melissa Rego Rodrigues', True, 'white')
nome2 = fonteNomes.render('Murilo Gonçalves de Lucena', True, 'white')
nome3 = fonteNomes.render('Eloise Sophia Lamenha Lins', True, 'white')
nome4 = fonteNomes.render('Ana Julia Figueredo Bernardo', True, 'white')
nome5 = fonteNomes.render('Anna Beatriz Batista Ramos', True, 'white')
nome6 = fonteNomes.render('Paula Beatriz Lucas Oliveira', True, 'white')


buttonBack = pygame.Rect(335, 500, largura_botao, altura_botao)
borderbuttonBack = pygame.Rect(330, 495, largura_botao + 10, altura_botao + 10)

bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img,(tela_largura, tela_comprimento))

while True:
    tela.blit(bg_img_resize, (0, 0))

    tela.blit(tituloCreditos, (270, 40))

    tela.blit(nome1, (350, 220))
    tela.blit(nome2, (335, 250))
    tela.blit(nome3, (330, 280))
    tela.blit(nome4, (310, 310))
    tela.blit(nome5, (310, 340))
    tela.blit(nome6, (320, 370))

    for events in pygame.event.get(): #botao back
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN: #cursor em cima do botao
            if buttonBack.collidepoint(events.pos): #cursor aperta o botao
                click.play()
                exec(open("FIELLI.py").read())
    k,w = pygame.mouse.get_pos()
    if buttonBack.x <= k <= buttonBack.x + largura_botao and buttonBack.y <= w <= buttonBack.y + altura_botao: #cursor em cima do botao
        pygame.draw.rect(tela, (255, 255, 255), borderbuttonBack)
        pygame.draw.rect(tela, (255, 157, 24), buttonBack) #cor com mouse *
    else:
        pygame.draw.rect(tela, (255, 255, 255), borderbuttonBack)
        pygame.draw.rect(tela, (242, 106, 24), buttonBack) #cor sem mouse default *
    tela.blit(textoBotaoBack, (buttonBack.x + 75, buttonBack.y + 2)) #borda do botao

    pygame.display.update()
