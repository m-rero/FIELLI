import pygame

class Physic:
     # definimos: jogo(a quem será incrementado), tipo de funções, posições, tamanhos e velocidades
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]

    # definimos a atualização por frame, configurando uma "gravdidade artificial"
    def uptade(self, movimento=(0, 0)):
        frame_movimento = (movimento[0] + self.velocity[0], movimento[1] + self.velocity[1])

        # a posição é definida pelo movimento
        self.pos[0] += frame_movimento[0]
        self.pos[1] += frame_movimento[1]

    # aqui iremos unificar as funções:
    def render_1(self, surf):
        surf.blit(self.game.assets['jogador'], self.pos)