# Importação do Pygame
import pygame
import sys
import random

# Inicializa o pygame (necessário para o audio)
pygame.init()

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
        # Realizamos comparações para evitar que a cobrinha
        # vá no sentido contrário
        if evt.key == pygame.K_RIGHT and self.velocidade != [-50, 0]:
            self.velocidade = [50, 0]
        elif evt.key == pygame.K_LEFT and self.velocidade != [50, 0]:
            self.velocidade = [-50, 0]
        elif evt.key == pygame.K_UP and self.velocidade != [0, 50]:
            self.velocidade = [0, -50]
        elif evt.key == pygame.K_DOWN and self.velocidade != [0, -50]:
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

    def comer(self, cabeca, corpo):
        # Sortear o novo lugar da fruta na tela

        # Como são 800px de largura e cada bloco ocupada 50px,
        # vamos sortear entre 1 e 16 (porque 800 / 50 = 16)
        # A altura será entre 1 e 12 (porque 600 / 50 = 12)
        # Porém, vamos tirar 1 de cada, para não desenhar fora da tela
        # logo, teremos 15 e 11
        self.pos = (random.randint(1,15) * 50, random.randint(1,11) * 50)
        self.update()

        # Enquanto houver colisão da nova fruta, gera uma nova posição
        while pygame.sprite.spritecollide(self, corpo, False) or pygame.sprite.collide_rect(cabeca, self):
            self.pos = (random.randint(1,15) * 50, random.randint(1,11) * 50)
            self.update()

class CorpoParte(pygame.sprite.Sprite):
    def __init__(self, pos):
        # Inicializa o objeto como um sprite
        pygame.sprite.Sprite.__init__(self)

        # Carrega a imagem para o objeto
        self.image = pygame.image.load('graficos/corpo.png')

        # Define o retângulo do objeto
        self.rect = self.image.get_rect()

        # Posiciona a parte do corpo na tela
        self.rect.topleft = pos;

class Corpo(pygame.sprite.OrderedUpdates):
    def __init__(self):
        pygame.sprite.OrderedUpdates.__init__(self)

    def crescer(self, pos):
        self.add(CorpoParte(pos))

    def mover(self):
        partes = self.sprites()
        if len(partes):
            # Remove o último elemento (para andar)
            self.remove(partes[0])

            # Adiciona uma nova posição no início
            pos = cabeca.rect.topleft
            self.add(CorpoParte(pos))

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

# Cria o objeto para guardar o corpo da cobrinha
corpo = Corpo()

# Variável para crescimento do corpo
crescerPos = False

# Carrega o beep (som para comer a fruta)
sfx_beep = pygame.mixer.Sound('sons/beep.wav')

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
            if cabeca.velocidade != [0, 0]:
                cabeca.muda_direcao(evento)

    # Desenha o fundo
    tela.blit(fundo, (0,0))

    # Atualiza a posição dos elementos na tela
    if cabeca.velocidade != [0, 0]:
        corpo.mover()
        cabeca.update()
        fruta.update()

    if crescerPos and crescerPos != cabeca.rect.topleft:
        corpo.crescer(crescerPos)
        crescerPos = False

    # Colisão entre a personagem e a fruta (comer a fruta)
    if pygame.sprite.collide_rect(cabeca, fruta):
        fruta.comer(cabeca, corpo)
        sfx_beep.play()

        # Espera até o próximo ciclo para aumentar o corpo
        # e evitar colisão automática com a cabeça
        crescerPos = cabeca.rect.topleft

    # Colisão da personagem com o corpo
    if pygame.sprite.spritecollide(cabeca, corpo, False):
        cabeca.velocidade = [0, 0]

    # Desenha a cabeça na tela
    tela.blit(cabeca.image, cabeca.rect)

    # Desenha o corpo na tela
    corpo.draw(tela)

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
