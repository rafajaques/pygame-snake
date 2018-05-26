# Importação do Pygame
import pygame
import sys
import random

# Classes para a personagem
class Cabeca(pygame.sprite.Sprite):
    def __init__(self):
        # Inicializa o objeto como um sprite
        pygame.sprite.Sprite.__init__(self)

        # Carrega a imagem para o objeto
        self.image = pygame.image.load('graficos/cabeca.png')

        # Define o retângulo do objeto
        self.rect = self.image.get_rect()

        # Velocidade do movimento
        self.velocidade = [50, 0]

    def update(self):
        # Gera o movimento
        self.rect.move_ip(self.velocidade)

        # Se passar para fora da tela, para todos os movimentos
        if self.rect.right > tela_largura or self.rect.left < 0 or self.rect.top < 0 or self.rect.bottom > tela_altura:
            self.velocidade = [0, 0]

    def muda_direcao(self, evt):
        if evt.key == pygame.K_RIGHT:
            self.velocidade = [50, 0]
        elif evt.key == pygame.K_LEFT:
            self.velocidade = [-50, 0]
        elif evt.key == pygame.K_UP:
            self.velocidade = [0, -50]
        elif evt.key == pygame.K_DOWN:
            self.velocidade = [0, 50]

# Classes para a personagem
class Fruta(pygame.sprite.Sprite):
    def __init__(self):
        # Inicializa o objeto como um sprite
        pygame.sprite.Sprite.__init__(self)

        # Carrega a imagem para o objeto
        self.image = pygame.image.load('graficos/fruta.png')

        # Define o retângulo do objeto
        self.rect = self.image.get_rect()

        # Define a posição da fruta na tela
        self.pos = (150,150)

    def update(self):
        # Posiciona o retangulo no lugar em que a fruta é desenhada
        self.rect.topleft = self.pos

    def comer(self):
        # Sortear o novo lugar da fruta na tela

        # Como são 800px de largura e cada bloco ocupada 50px,
        # vamos sortear entre 1 e 16 (porque 800 / 50 = 16)
        # A altura será entre 1 e 12 (porque 600 / 50 = 12)
        # Porém, vamos tirar 1 de cada, para não desenhar fora da tela
        # logo, teremos 15 e 11
        self.pos = (random.randint(1,15) * 50, random.randint(1,11) * 50)


# Dimensões da tela (em pixels)
tela_largura = 800
tela_altura = 600
fundo = pygame.image.load('graficos/fundo.png')
clock = pygame.time.Clock()

# Criação da tela
tela = pygame.display.set_mode((tela_largura, tela_altura))

# Título da janela
pygame.display.set_caption('Jogo da Cobrinha');

# Esconde o ponteiro do mouse
pygame.mouse.set_visible(False)

# Cria o objeto com a cabeça da cobrinha
cabeca = Cabeca()

# Cria uma fruta para ser comida
fruta = Fruta()

# Iniciar jogo (repetição infinita)
while True:
    # Ajustar FPS
    clock.tick(5)

    # Eventos do jogo
    for evento in pygame.event.get():
        # Evento de fechar a tela
        if evento.type == pygame.QUIT:
            sys.exit()

        # Eventos de teclado
        elif evento.type == pygame.KEYDOWN:
            cabeca.muda_direcao(evento)

    # Desenha o fundo
    tela.blit(fundo, (0,0))

    # Atualiza a posição dos elementos na tela
    cabeca.update()
    fruta.update()

    # Colisão entre a personagem e a fruta
    if pygame.sprite.collide_rect(cabeca, fruta):
        fruta.comer()

    # Desenha a cabeça na tela
    tela.blit(cabeca.image, cabeca.rect)

    # Desenha a fruta
    tela.blit(fruta.image, fruta.pos)

    # Pararam os movimentos?
    if cabeca.velocidade == [0, 0]:
        pygame.font.init()
        fonte = pygame.font.SysFont("Arial", 130)
        label = fonte.render("Fim de jogo!" , 1, [0,0,0])
        # Posicionar no centro
        label_rect = label.get_rect()
        label_rect.center = (tela_largura / 2, tela_altura / 2)
        tela.blit(label, label_rect)

    pygame.display.flip()
