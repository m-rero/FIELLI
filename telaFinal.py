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
pygame.display.set_caption('FIM') #legenda da tela

#som
click = pygame.mixer.Sound('sons/click.mp3')
pygame.mixer.init()
pygame.mixer.music.load('sons/New_Super_Mario_Bros.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

altura_botao = 80
largura_botao = 330

fonteTitulo = pygame.font.Font('script/fontes/OMORI-GAME2.ttf', 200) #fonte do título
fontegame = pygame.font.Font('script/fontes/Retro Gaming.ttf ', 60) #fonte do botao
fonteNomes = pygame.font.Font('script/fontes/OMORI-GAME2.ttf', 40) 
docente = fonteNomes.render('Docente: Adauto Trigueiro Almeida Filho', True, 'white')
discentes = fonteNomes.render('Discentes:', True, 'white')
nome1 = fonteNomes.render('Ana Julia Figueredo Bernardo', True, 'white')
nome2 = fonteNomes.render('Anna Beatriz Batista Ramos', True, 'white')
nome3 = fonteNomes.render('Eloise Sophia Lamenha Lins', True, 'white')
nome4 = fonteNomes.render('Melissa Rego Rodrigues', True, 'white')
nome5 = fonteNomes.render('Murilo Goncalves de Lucena', True, 'white')
nome6 = fonteNomes.render('Paula Beatriz Lucas Oliveira', True, 'white')
thanks = fonteNomes.render('OBRIGADO POR JOGAR! :3', True, 'white')

textobotao1 = fontegame.render('MENU', True, 'white') #renderizar o botao na superficie
titulo = fonteTitulo.render('FIM', True, (255, 180, 24))

button1 = pygame.Rect(335, 570, largura_botao, altura_botao) #retangulo do botao posicao, posicao, tamanho largura, tamanho altura
borderbutton1 = pygame.Rect(330, 565, largura_botao + 10, altura_botao + 10) #da borda

bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img,(tela_largura, tela_comprimento))

while True:
    tela.blit(bg_img_resize, (0, 0))

    tela.blit(titulo, (400, -30)) #titulo

    tela.blit(docente, (250, 150))
    tela.blit(discentes, (430, 220))
    tela.blit(nome1, (300, 250))
    tela.blit(nome2, (300, 280))
    tela.blit(nome3, (318, 310))
    tela.blit(nome4, (335, 340))
    tela.blit(nome5, (315, 370))
    tela.blit(nome6, (310, 400))
    tela.blit(thanks, (350, 500))

    for events in pygame.event.get(): #botao menu
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN: #cursor em cima do botao
            if button1.collidepoint(events.pos): #cursor aperta o botao
                click.play()
                exec(open("menu funcional.py").read())

    a,b = pygame.mouse.get_pos()
    if button1.x <= a <= button1.x + largura_botao and button1.y <= b <= button1.y + altura_botao: #cursor em cima do botao
        pygame.draw.rect(tela, (255, 255, 255), borderbutton1)
        pygame.draw.rect(tela, (255, 157, 24), button1) #cor com mouse *
    else:
        pygame.draw.rect(tela, (255, 255, 255), borderbutton1)
        pygame.draw.rect(tela, (242, 106, 24), button1) #cor sem mouse default *
    tela.blit(textobotao1, (button1.x + 70, button1.y + 2)) #borda do botao

    pygame.display.update()
    
# Música Para
pygame.mixer.music.stop()
pygame.mixer.quit()
