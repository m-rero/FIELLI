import sys
import pygame

class Jogo:
    def __init__(self):

        pygame.init()
        #definição do nome e resolução
        pygame.display.set_caption('FIELLI')
        self.screen = pygame.display.set_mode((1024, 768))
        #definição do icone do executável
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()

    def run(self):
        #definir abrir e fechar o executável
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #definir a atualização em frames (60fps)
            pygame.display.update()
            self.clock.tick(60)
#retornar o jogo "rodando":
Jogo().run()
