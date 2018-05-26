# Importação do Pygame
import pygame
import sys

#  Dimensões da tela (em pixels)
tela_largura = 800
tela_altura = 600

# Criação da tela
tela = pygame.display.set_mode((tela_largura, tela_altura))

# Título da janela
pygame.display.set_caption('Jogo da Cobrinha');

# Iniciar jogo (repetição infinita)
while True:
    # Eventos do jogo
    for evento in pygame.event.get():
        # Evento de fechar a tela
        if evento.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
