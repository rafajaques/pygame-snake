# Importação do Pygame
import pygame
import sys

# Dimensões da tela (em pixels)
tela_largura = 800
tela_altura = 600
fundo = pygame.image.load('graficos/fundo.png')

# Criação da tela
tela = pygame.display.set_mode((tela_largura, tela_altura))

# Título da janela
pygame.display.set_caption('Jogo da Cobrinha');

# Esconde o ponteiro do mouse
pygame.mouse.set_visible(False)

# Iniciar jogo (repetição infinita)
while True:
    # Eventos do jogo
    for evento in pygame.event.get():
        # Evento de fechar a tela
        if evento.type == pygame.QUIT:
            sys.exit()

    tela.blit(fundo, (0,0))

    pygame.display.flip()
