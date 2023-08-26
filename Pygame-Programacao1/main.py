import pygame
import pickle
from os import path

pygame.init()
# Definição do nome, resolução e o display(interativo)
pygame.display.set_caption('FIELLI')
# Tela do jogo e configurações
tile_size = 50
fps = 60
cols = 20
margin = 100
tela_largura = tile_size * cols
tela_comprimento = (tile_size * cols) - 400 + margin
level = 1
max_levels = 7  

tela = pygame.display.set_mode((tela_largura, tela_comprimento))

# Definição do clock do jogo
clock = pygame.time.Clock()

# Definição do icone do executável
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#barra de pontuacao
pontuacao = 0
font = pygame.font.Font(None, 36) 

# Carregando imagens fundo
bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img,(tela_largura, tela_comprimento))

# Music begin
pygame.mixer.init()
pygame.mixer.music.load('sons/intro.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#Sons
pulo = pygame.mixer.Sound('sons/cat.mp3')
pulo.set_volume(0.1)

def reset_level(level):
	player.reset(100, tela_comprimento - 130)

	# Load in level data and create world
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

		# Get mouse position
		pos = pygame.mouse.get_pos()

		# Check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		# Draw button
		tela.blit(self.image, self.rect)

		return action

class World():
	def __init__(self, data):
		self.tile_list = []

		# Load images
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
					# Plataforma
					img = pygame.transform.scale(plataforma, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				elif tile == 3:
					# Fogo
					img = pygame.transform.scale(fogo, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				elif tile == 4:
					# Ouro
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
		# Frames do gatinho(personagem) em diversas posições
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
		self.on_ground = False
		self.jump_power = -15
		self.frames = []

		#Dedica-se aqui apenas para a animação dos sprites:

		self.frames_right = []  # Quadros de animação para a direção direita
		self.frames_left = []  # Quadros de animação para a direção esquerda

		player_scale = 60
		for frame_number in range(3, 5):
			frame_image = pygame.transform.scale(
				pygame.image.load(f'img/gato/spritesfielli/{frame_number}.png'),
				(5 * player_scale, 8 * player_scale)
			)
			self.frames_right.append(frame_image)
			self.frames.append(frame_image)

			self.frame_index = 0
			self.image = pygame.transform.scale(self.frames[self.frame_index], (80, 80))

			frame_image_left = pygame.transform.flip(frame_image, True, False)
			self.frames_left.append(frame_image_left)

			self.frame_index = 0
			self.direction = "right"
			self.image = pygame.transform.scale(self.frames_right[self.frame_index], (80, 80))

		self.frames_jump_right = []  # Quadros de animação para pular a direita
		self.frames_jump_left = []  # Quadros de animação para pular a esquerda
		self.frames_jump_right = []  # Quadros de animação para pular a direita
		self.frames_jump_left = []  # Quadros de animação para pular a esquerda

		for frame_number in range(9, 10):  # Use os números apropriados para os frames de pulo
			frame_image = pygame.transform.scale(
				pygame.image.load(f'img/gato/spritesfielli/{frame_number}.png'),
				(5 * player_scale, 8 * player_scale)
			)
			self.frames_jump_right.append(frame_image)

			frame_image_left = pygame.transform.flip(frame_image, True, False)
			self.frames_jump_left.append(frame_image_left)

	def update(self):
		dx = 0
		dy = 0

		# Captura as teclas pressionadas
		teclas = pygame.key.get_pressed()

		# Verificar colisão com o solo (plataformas)
		self.on_ground = False
		for tile in world.tile_list:
			if tile[1].colliderect(self.rect.x, self.rect.y + 1, self.largura, self.altura):
				self.on_ground = True
				break

		# Move o gato com base nas teclas pressionadas
		if teclas[pygame.K_LEFT]:
			dx -= self.velocidade_x
		if teclas[pygame.K_RIGHT]:
			dx += self.velocidade_x

		# Lógica de pulo
		if self.on_ground and teclas[pygame.K_SPACE]:
			self.vel_y = self.jump_power
			pulo.play()
		if self.on_ground and teclas[pygame.K_SPACE]:
			self.vel_y = self.jump_power
			pulo.play()
			self.pulando = True
		else:
			self.pulando = False

		# Aqui as funcionalidades das animações:
		if teclas[pygame.K_LEFT] or teclas[pygame.K_RIGHT]:
			if teclas[pygame.K_LEFT]:
				self.direction = "left"
			else:
				self.direction = "right"

			self.frame_index += 0.2
			if self.direction == "left":
				frames_list = self.frames_left
			else:
				frames_list = self.frames_right

			if self.frame_index >= len(frames_list):
				self.frame_index = 0

			self.image = pygame.transform.scale(frames_list[int(self.frame_index)], (80, 80))

		if self.on_ground and teclas[pygame.K_SPACE]:
			self.vel_y = self.jump_power
			pulo.play()

		if self.pulando:
			if self.direction == "left":
				frames_jump_list = self.frames_jump_left

			else:
				frames_jump_list = self.frames_jump_right

			self.frame_index += 0.2
			if self.frame_index >= len(frames_jump_list):
				self.frame_index = 0

			self.image = pygame.transform.scale(frames_jump_list[int(self.frame_index)], (80, 80))

		# Gravidade
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		dy += self.vel_y

		# Checar colisão
		for tile in world.tile_list:
			# Checar colisão em x | tile[1] = solo rocha
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.largura, self.altura):
				dx = 0
			# Checar colisão em y
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.largura, self.altura):
				# Checar se está pulando
				if self.vel_y < 0:
					dy = tile[1].bottom - self.rect.top
				# Checar se está caindo
				elif self.vel_y >= 0:
					dy = tile[1].top - self.rect.bottom
					self.vel_y = 0
				
		# Atualizar coordenadas do jogador
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

		# Desenhar jogador na tela
		tela.blit(self.image, self.rect)

player = Player(0, 460)

def reset_level(level):
	player.reset(100, tela_comprimento - 460)
	

# Carregar data nível
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

	#pontuacao
	pygame.draw.rect(tela, (255, 255, 255), (880, 20, 100, 22))    
		
	# Renderizar o texto da pontuação
	texto_pontuacao = font.render('peças: ' + str(pontuacao), False, (0, 0, 0))
	tela.blit(texto_pontuacao, (882, 20)) 
	
	

	pygame.display.update()
 
# Music stop
pygame.mixer.music.stop()
pygame.mixer.quit()

pygame.quit()
