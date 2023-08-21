import sys
import pygame

from script.entidades import Physic

class Jogo:
    def __init__(self):
        pygame.init()
        # definição do nome, resolução e o display(interativo)
        pygame.display.set_caption('FIELLI')
        self.screen = pygame.display.set_mode((1024, 768))
        self.display = pygame.Surface((320, 240))
        # definição do clock do jogo#
        self.clock = pygame.time.Clock()

        # definição do icone do executável
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)

        # aqui estão as definições do objeto do personagem
        self.img = pygame.image.load('datagame/sprites/fiellibase1.png')
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [160, 260]
        self.movimento = [False, False]

        # aqui estão o assets do jogador(onde será carregado o sprite)
        self.assets = {
            'jogador': pygame.image.load('datagame/sprites/fiellibase1.png')
        }
        # aqui as definições do objeto de colisão:
        self.colissao_area = pygame.Rect(50, 50, 300, 50)

        self.player = Physic(self, 'player', (50, 50), (1, 1))


    def run(self):
        while True:
            self.display.fill((14, 219, 248))

            self.player.uptade((self.movimento[1] - self.movimento[0], 0))
            self.player.render_1(self.display)

            # definição da abertura e fechamento do executável
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # aqui o user vai conseguir interagir com o "WASD"
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_a:
                        self.movimento[0] = True
                    if evento.key == pygame.K_d:
                        self.movimento[1] = True
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_a:
                        self.movimento[0] = False
                    if evento.key == pygame.K_d:
                        self.movimento[1] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Jogo().run()
