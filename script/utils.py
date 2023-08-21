import pygame

BASE_IMG_PATH = 'projetofielli_ilmoruuu/datagame/sprites'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0 ,0))
    return img