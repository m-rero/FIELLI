import pygame
import pickle
from os import path

pygame.init()
# definição do nome, resolução e o display(interativo)
pygame.display.set_caption('FIELLI')
#tela do jogo e configurações
tile_size = 50
fps = 60
cols = 20
margin = 100
tela_largura = tile_size * cols
tela_comprimento = (tile_size * cols) - 400 + margin
level = 1
max_levels = 7

tela = pygame.display.set_mode((tela_largura, tela_comprimento))

# definição do clock do jogo#
clock = pygame.time.Clock()

# definição do icone do executável
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#carregando imagens fundo 
bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img,(tela_largura, tela_comprimento))


def reset_level(level):
	player.reset(100, tela_comprimento - 130)

	#load in level data and create world
	if path.exists(f'level{level}_data'):
		pickle_in = open(f'level{level}_data', 'rb')
		world_data = pickle.load(pickle_in)
	world = World(world_data)

	return world

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		#draw button
		tela.blit(self.image, self.rect)

		return action

class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		rocha = pygame.image.load('img/bloco.png')
		plataforma = pygame.image.load('img/plaforma.jpg')
		ouro = pygame.image.load('img/ouro.png')
		fogo = pygame.image.load('img/fogo.png')
		
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(rocha, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				elif tile == 2:
					#plataforma
					img = pygame.transform.scale(plataforma, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				elif tile == 3:
					#fogo
					img = pygame.transform.scale(fogo, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				elif tile == 4:
					#ouro
					img = pygame.transform.scale(ouro, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)

				col_count += 1
			row_count += 1


	def draw(self):
		for tile in self.tile_list:
			tela.blit(tile[0], tile[1])
			pygame.draw.rect(tela, (255, 255, 255), tile[1], 2)

class Player():
	def __init__(self, x, y):
		#frames do gatinho(personagem) em diversas posições
		frames = []
		player_scale = 60
		for _ in range(1, 6):
			frames.append(pygame.transform.scale(pygame.image.load(f'img/gato/spritesfielli/{_}.png'), (5 * player_scale, 8 * player_scale)))
		img = frames[0]
		self.image = pygame.transform.scale(img, (80, 80))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.largura = self.image.get_width()
		self.altura = self.image.get_height()
		self.vel_y = 0
		self.velocidade_x = 5
		self.pulando = False
		

	def update(self):
		dx = 0
		dy = 0

		# Captura as teclas pressionadas
		teclas = pygame.key.get_pressed()
		
		# Move o gato com base nas teclas pressionadas
		if teclas[pygame.K_LEFT]:
			dx -= self.velocidade_x
		if teclas[pygame.K_RIGHT]:
			dx += self.velocidade_x
			
		# Lógica de pulo
		if not self.pulando and teclas[pygame.K_SPACE]:  # Pressionar a barra de espaço para pular
			self.pulando = True
			self.vel_y = -15
		if teclas[pygame.K_SPACE] == False:
			self.pulando = False

		#gravidade
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		dy += self.vel_y

		#checar colisão
		for tile in world.tile_list:
			#checar colisão em x | tile[1] = solo rocha
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.largura, self.altura):
				dx = 0
			#checar colisão em y
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.largura, self.altura):
				#checar se está pulando
				if self.vel_y < 0:
					dy = tile[1].bottom - self.rect.top
				#checar se está caindo
				elif self.vel_y >= 0:
					dy = tile[1].top - self.rect.bottom
					self.vel_y = 0
				

		#atualizar coordenadas do jogador
		self.rect.x += dx
		self.rect.y += dy

		# Verifique os limites horizontais
		if self.rect.x < 0:
			self.rect.x = 0
		elif self.rect.x > tela_largura - self.largura:
			self.rect.x = tela_largura - self.largura
		
		# Verifique os limites verticais
		if self.rect.y < 0:
			self.rect.y = 0
		elif self.rect.y > tela_comprimento - self.altura:
			self.rect.y = tela_comprimento - self.altura
   

		#desenhar jogador na tela
		tela.blit(self.image, self.rect)
	 

player = Player(0, 460)

def reset_level(level):
	player.reset(100, tela_comprimento - 460)
	

#carregar data nível
if path.exists(f'niveis/level{level}_data'):
	pickle_in = open(f'niveis/level{level}_data', 'rb')
	world_data = pickle.load(pickle_in)
world = World(world_data)

run = True
while run:

	clock.tick(fps)
	
	tela.blit(bg_img_resize, (0, 0))
	
	world.draw()
	player.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			
	pygame.display.update()

pygame.quit()