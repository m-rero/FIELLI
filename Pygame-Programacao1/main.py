# Imports
import pygame
import pickle
from os import path

# Inicio do jogo
pygame.init()
pygame.display.set_caption('FIELLI')

# Tela do jogo e Configurações
tile_size = 50
fps = 60
cols = 20
margin = 100
tela_largura = tile_size * cols
tela_comprimento = (tile_size * cols) - 400 + margin
level = 1
max_levels = 4
tela = pygame.display.set_mode((tela_largura, tela_comprimento))

# Pontuação
pontuacao = 0
font = pygame.font.Font(None, 36)

# Clock do jogo
clock = pygame.time.Clock()

# Icone do executável
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Variável para controlar a exibição da mensagem de nível
exibir_mensagem_nivel = True

# Imagens
bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img,(tela_largura, tela_comprimento))
peca1 = pygame.image.load('img/peca1.png')
peca1_x = 0
peca1_y = 0
peca2 = pygame.image.load('img/peca2.png')
peca2_x = 0
peca2_y = 0
rocha = pygame.image.load('img/bloco.png')
pecas = [peca1, peca2]
fogo = pygame.image.load('img/fogo.png')
foguete = pygame.image.load('img/foguete2.png')
fogueteativo = pygame.image.load('img/foguete1.png')

# Música inicia
pygame.mixer.init()
pygame.mixer.music.load('sons/intro.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Sound Effects
pulo = pygame.mixer.Sound('sons/cat.mp3')
click = pygame.mixer.Sound('sons/click.mp3')
pegar = pygame.mixer.Sound('sons/pick.mp3')

# Niveis
def reset_world(level):
	# Recarregue os dados do nível (se necessário)
	if path.exists(f'niveis/level{level}_data'):
		pickle_in = open(f'niveis/level{level}_data', 'rb')
		world_data = pickle.load(pickle_in)

	# Limpe os grupos de sprites (se necessário)
	plataforma_grupo.empty()
	peca_grupo.empty()
	foguete_grupo.empty()
	fogueteativo_grupo.empty()

	# Reinicie o estado do jogador (se necessário)
	player.reset(tile_size, tile_size)
	return world

def reset_level(level):
	player.reset(100, tela_largura - 130)
	plataforma_grupo.empty()
	peca_grupo.empty()
	foguete_grupo.empty()
	fogueteativo_grupo.empty()

	#load in level data and create world
	if path.exists(f'niveis/level{level}_data'):
		pickle_in = open(f'niveis/level{level}_data', 'rb')
		world_data = pickle.load(pickle_in)
	
	world = World(world_data)
	
	return world

# Botões
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


# Mundo
class World():
	def __init__(self, data):
		self.tile_list = []

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
					#self, x, y, mover_x, mover_y --> definicao x, y coordenadas e movimento vertical ou horizontal das plataformas (0,1 - vertical e 1,0 - horizontal)
					plataforma = Plataforma(col_count * tile_size, row_count * tile_size, 1, 0)
					plataforma_grupo.add(plataforma)
				elif tile == 3:
					#plataforma
					plataforma = Plataforma(col_count * tile_size, row_count * tile_size, 0, 1)
					plataforma_grupo.add(plataforma)
				elif tile == 4:
					#fogo
					img = pygame.transform.scale(fogo, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				elif tile > 4 and tile <= 6:
					#pecas
					peca = Peca(col_count * tile_size, row_count * tile_size )
					peca_grupo.add(peca)

				elif tile == 7:
					#foguete
					foguete = Foguete(col_count * tile_size, row_count * tile_size )
					foguete_grupo.add(foguete)

				col_count += 1
			row_count += 1
	def draw(self):
		for tile in self.tile_list:
			tela.blit(tile[0], tile[1])
			pygame.draw.rect(tela, (255, 255, 255), tile[1], 2)

# Plataforma
class Plataforma(pygame.sprite.Sprite):
	#definindo variáveis
	def __init__(self, x, y, mover_x, mover_y):
		pygame.sprite.Sprite.__init__(self)
		#carregar imagem de rocha e transformar em tamanho de plataforma
		img = pygame.image.load('img/bloco.png')
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
		#transformar em objeto retângulo para colisão
		self.rect = self.image.get_rect()
		#chamar coordenadas
		self.rect.x = x
		self.rect.y = y
		self.mover_contra = 0
		self.mover_direcao = 1
		self.mover_x = mover_x
		self.mover_y = mover_y

	def update(self):
		#criar movimento com os valores definidos
		self.rect.x += self.mover_direcao * self.mover_x
		self.rect.y += self.mover_direcao * self.mover_y
		self.mover_contra += 1
		#movimento de ida e volta da plataforma - definicao de limite de movimento antes de inventer direcao
		if abs(self.mover_contra) > 50:
			self.mover_direcao *= -1
			self.mover_contra *= -1

# Peças
class Peca(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		for _ in range(1,2):
			img = pygame.image.load(f'img/peca{_}.png')
			self.image = pygame.transform.scale(img, (tile_size * (5/6), tile_size * (5/6)))
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y
class Foguete(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		for _ in range(1,2):
			img = pygame.image.load(f'img/foguete{2}.png')
			self.image = pygame.transform.scale(img, (tile_size // 0.5, tile_size // 0.5))
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y

# Jogador
class Player():
	def __init__(self, x, y):
		self.reset(x, y)

	def update(self):
		dx = 0
		dy = 0
		col_thresh = 20

		# Teclas
		# Move o gato com base nas teclas pressionadas
		teclas = pygame.key.get_pressed()
		if teclas[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
			pulo.play()
			self.vel_y = -15
			self.jumped = True
		if teclas[pygame.K_SPACE] == False:
			self.jumped = False
		if teclas[pygame.K_LEFT]:
			dx -= self.velocidade_x
		if teclas[pygame.K_RIGHT]:
			dx += self.velocidade_x

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
		self.in_air =  True
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
					self.in_air = False

		# Checar colisão com as plataformas
		for plataforma in plataforma_grupo:
			#colisão em direcao x
			if plataforma.rect.colliderect(self.rect.x + dx, self.rect.y, self.largura, self.altura):
				dx = 0
			#colisao em direcao y
			if plataforma.rect.colliderect(self.rect.x, self.rect.y + dy, self.largura, self.altura):
				#checar se player esta abaixo da plataforma
				if abs((self.rect.top + dy) - plataforma.rect.bottom) < col_thresh:
					self.vel_y = 0
					dy = plataforma.rect.bottom - self.rect.top
				#checar se player esta em cima da plataforma
				elif abs((self.rect.bottom + dy) - plataforma.rect.top) < col_thresh:
					self.rect.bottom = plataforma.rect.top
					self.in_air = False
					dy = 0
				#mover (em x - horizontal) com a plataforma
				if plataforma.mover_x != 0:
					self.rect.x += plataforma.mover_direcao

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

	def reset(self, x, y):
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
		self.pulando  = False
		self.direction = 0
		self.in_air = True
		self.index = 0
		self.counter = 0
		self.velocidade_x = 4
		self.frames = []

		#Dedica-se aqui apenas para a animação dos sprites:

		self.frames_right = []  # Quadros de animação para a direção direita
		self.frames_left = []  # Quadros de animação para a direção esquerda


		for frame_number in range(3, 5):
			frame_image = pygame.transform.scale(
				pygame.image.load(f'img/gato/spritesfielli/{frame_number}.png'),
				(80,80)
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

		for frame_number in range(9, 10):  # Use os números apropriados para os frames de pulo
			frame_image = pygame.transform.scale(
				pygame.image.load(f'img/gato/spritesfielli/{frame_number}.png'),
				(80,80)
			)
			self.frames_jump_right.append(frame_image)

			frame_image_left = pygame.transform.flip(frame_image, True, False)
			self.frames_jump_left.append(frame_image_left)

player = Player(0, 460)

plataforma_grupo = pygame.sprite.Group()
peca_grupo = pygame.sprite.Group()
foguete_grupo = pygame.sprite.Group()
fogueteativo_grupo = pygame.sprite.Group()

# Carregar "data-nível"
if path.exists(f'niveis/level{level}_data'):
	pickle_in = open(f'niveis/level{level}_data', 'rb')
	world_data = pickle.load(pickle_in)
world = World(world_data)

# Main loop
run = True
while run:

	clock.tick(fps)

	tela.blit(bg_img_resize, (0, 0))

	# Mensagens dos Níveis
	mensagens_nivel = {
		1: "Um novo mundo",
		2: "De pulo em pulo...",
		3: "''Picos aranhadores''",
		4: "Plataformas remexidas",
		5: "Mensagem para nível 5",
		6: "Mensagem para nível 6",
		7: "Mensagem para nível 7",
		8: "Mensagem para nível 8",
		9: "Mensagem para nível 9",
		10: "Mensagem para nível 10",
	}

	if exibir_mensagem_nivel:
		fontegame = pygame.font.Font('script/fontes/OMORI-GAME2.ttf ', 25)
		mensagem = fontegame.render(f"Nivel {level} - {mensagens_nivel.get(level)}", True, (255, 255, 255))
		tela.blit(mensagem,(tela_largura // 2 - mensagem.get_width() // 2, tela_comprimento // 2 - mensagem.get_height() // 2))
		pygame.display.update()

		esperando = True
		while esperando:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					esperando = False

		exibir_mensagem_nivel = False

	tela.blit(bg_img_resize, (0, 0))

	world.draw()
	player.update()

	plataforma_grupo.update()
	plataforma_grupo.draw(tela)

	peca_grupo.update()
	peca_grupo.draw(tela)

	foguete_grupo.update()
	foguete_grupo.draw(tela)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# Pontuação
	pygame.draw.rect(tela, (255, 255, 255), (890, 20, 100, 21))

	# Renderizar o texto da pontuação
	fontegame = pygame.font.Font('script/fontes/OMORI-GAME2.ttf ', 25)
	texto_pontuacao = fontegame.render('Partes: ' + str(pontuacao), False, (0, 0, 0))
	tela.blit(texto_pontuacao, (892, 17))

	colisoes = pygame.sprite.spritecollide(player, peca_grupo, True)

	# Atualize a pontuação com base nas colisões
	for partes in colisoes:
		pontuacao += 1
		click.play()

	if pontuacao == 5:
		level += 1
		if level <= max_levels:
			# Reset level
			pontuacao -= 5
			pygame.time.delay(100)
			world_data = []
			world = reset_level(level)
			exibir_mensagem_nivel = True

	pygame.display.update()

# Música Para
pygame.mixer.music.stop()
pygame.mixer.quit()

pygame.quit()
