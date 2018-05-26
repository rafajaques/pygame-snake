# Importação do Pygame
import pygame
import sys

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
        if self.rect.right > tela_largura:
            self.velocidade = [0, 0]


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

# Iniciar jogo (repetição infinita)
while True:
    # Ajustar FPS
    clock.tick(5)

    # Eventos do jogo
    for evento in pygame.event.get():
        # Evento de fechar a tela
        if evento.type == pygame.QUIT:
            sys.exit()

    tela.blit(fundo, (0,0))

    cabeca.update()

    tela.blit(cabeca.image, cabeca.rect)

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
