import pygame
import pickle
from os import path


pygame.init()

clock = pygame.time.Clock()
fps = 60

#tela do jogo e configurações
tile_size = 50
cols = 20
margin = 100
tela_largura = tile_size * cols
tela_comprimento = (tile_size * cols) - 320 + margin

tela = pygame.display.set_mode((tela_largura, tela_comprimento))
pygame.display.set_caption('Level Editor')


#carregar imagens
bg_img = pygame.image.load('img/nivel1.png')
bg_img_resize = pygame.transform.scale(bg_img,(tela_largura, tela_comprimento))
bloco = pygame.image.load('img/bloco2.png')
rocha = pygame.image.load('img/bloco.png')
espinhos = pygame.image.load('img/espinhos.png')
salvar = pygame.image.load('img/save.png')
carregar = pygame.image.load('img/load.png')
peca1 = pygame.image.load('img/peca1.png')
peca2 = pygame.image.load('img/peca2.png')
pecas = [peca1, peca2]
foguete = pygame.image.load('img/foguete2.png.')
fogueteativo = pygame.image.load('img/foguete1.png')
#frames do gatinho(personagem) em diversas posições
frames = []
player_scale = 60
for _ in range(1, 12):
    frames.append(pygame.transform.scale(pygame.image.load(f'img/gato/spritesfielli/{_}.png'), (5 * player_scale, 8 * player_scale)))

#variáveis
clicked = False
nivel = 1

#cores
white = (255, 255, 255)


font = pygame.font.SysFont('Futura', 24)

#lista de tiles vazia
world_data = []
for row in range(20):
	r = [0] * 20
	world_data.append(r)

#criar limite de mundo
for tile in range(0, 20):
	world_data[19][tile] = 2
	world_data[0][tile] = 1
	world_data[tile][0] = 1
	world_data[tile][19] = 1

#output de texto na tela
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	tela.blit(img, (x, y))

#def draw_grid():
	#for linha in range(21):
		#vertical
	#	pygame.draw.line(tela, white, (linha * tile_size, 0), (linha * tile_size, tela_comprimento - margin))
		#horizontal
	#	pygame.draw.line(tela, white, (0, linha * tile_size), (tela_largura, linha * tile_size))


def draw_world():
	#rowxcol --> ixj em uma matriz por exemplo
	for row in range(20):
		for col in range(20):
			#0 é vazio
			if world_data[row][col] > 0:
				valor = world_data[row][col]
				if valor == 1:
					#rocha
					img = pygame.transform.scale(rocha, (tile_size, tile_size)) #ajustar imagem para tamanho da grid/tiles criada
					tela.blit(img, (col * tile_size, row * tile_size)) #mostrar a imagem 
				elif world_data[row][col] == 2:
					#plataforma move horizontal
					img = pygame.transform.scale(rocha, (tile_size, tile_size // 2))
					tela.blit(img, (col * tile_size, row * tile_size))
				elif world_data[row][col] == 3:
					#plataforma move
					img = pygame.transform.scale(rocha, (tile_size, tile_size // 2))
					tela.blit(img, (col * tile_size, row * tile_size))
				elif valor == 4:
					#espinhos
					img = pygame.transform.scale(espinhos	, (tile_size, int(tile_size * 0.75)))
					tela.blit(img, (col * tile_size, row * tile_size + (tile_size * 0.25)))
				elif valor == 5 or valor == 6:
					#pecas
					img = pygame.transform.scale(pecas[valor-5], (tile_size // 2, tile_size // 2))					
					tela.blit(img, (col * tile_size, row * tile_size))
				elif valor == 7:
					#foguete
					img = pygame.transform.scale(foguete, (tile_size // 0.5, tile_size // 0.5))
					tela.blit(img, (col * tile_size, row * tile_size))
				elif valor == 8:
					#fogueteativo
					img = pygame.transform.scale(fogueteativo, (tile_size // 0.5, tile_size // 0.5))
					tela.blit(img, (col * tile_size, row * tile_size))

				#elif valor <= 18:
				#	img = pygame.transform.scale(frames[valor-17], (tile_size, tile_size))
				#	tela.blit(img, (col * tile_size, row * tile_size + (tile_size)))
				


class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self):
		action = False

		#posição do mouse
		pos = pygame.mouse.get_pos()

		#checar condições do mouse
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#desenhar botão
		tela.blit(self.image, (self.rect.x, self.rect.y))

		return action

#botôes de salvar e carregar
save_button = Button(tela_largura // 2 - 150, tela_comprimento - 80, salvar)
load_button = Button(tela_largura // 2 + 50, tela_comprimento - 80, carregar)

#loop main
run = True
while run:

	clock.tick(fps)

	#background
	tela.blit(bg_img_resize, (0, 0))

	#carregar e salvar nível
	if save_button.draw():
		#salvar data de nível
		pickle_out = open(f'level{nivel}_data', 'wb')
		pickle.dump(world_data, pickle_out)
		pickle_out.close()
	if load_button.draw():
		#carregar data de nível
		if path.exists(f'level{nivel}_data'):
			pickle_in = open(f'level{nivel}_data', 'rb')
			world_data = pickle.load(pickle_in)


	#desenhar
	#draw_grid()
	draw_world()


	#texto mostrando nível atual
	draw_text(f'Level: {nivel}', font, white, tile_size, tela_comprimento - 60)
	draw_text('Press UP or DOWN to change level', font, white, tile_size, tela_comprimento - 40)

	#event handler
	for event in pygame.event.get():
		#sair do jogo
		if event.type == pygame.QUIT:
			run = False
		#mouseclicks para mudar tiles
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
			pos = pygame.mouse.get_pos()
			x = pos[0] // tile_size
			y = pos[1] // tile_size
			#checar coordenadas
			if x < 20 and y < 20:
				#atualizar status dos tiles
				if pygame.mouse.get_pressed()[0] == 1:
					world_data[y][x] += 1
					if world_data[y][x] > 10:
						world_data[y][x] = 0
				elif pygame.mouse.get_pressed()[2] == 1:
					world_data[y][x] -= 1
					if world_data[y][x] < 0:
						world_data[y][x] = 9
		if event.type == pygame.MOUSEBUTTONUP:
			clicked = False
		#setas baixo e cima para mudar nível
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				nivel += 1
			elif event.key == pygame.K_DOWN and nivel > 1:
				nivel -= 1

	#update game display window
	pygame.display.update()

pygame.quit()
