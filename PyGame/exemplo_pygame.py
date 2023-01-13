#Importando 
import pygame
import pandas
from pygame.locals import *
import sys
from pathlib import Path

#Constantes
preto = (0,0,0)
largura_janela = 640
altura_janela = 480
frames_por_segundo = 30

CAMINHO_BASE = Path(__file__).resolve().parent
CAMINHO_BASE = str(CAMINHO_BASE)
print(CAMINHO_BASE)
caminho_imagem_bola = CAMINHO_BASE + '\imagens\\ball.png'

#3. Inicializa o mundo
pygame.init()
janela = pygame.display.set_mode((largura_janela, altura_janela))
relogio = pygame.time.Clock()

#4. Roda os assets
imagem_bola = pygame.image.load(caminho_imagem_bola)

#5. Inicializa as variáveis

#6. Loop 
while True:
    
    #7. Checar e lidar com eventos
    for evento in pygame.event.get():
        
        #clicou o botao de fechar? Fecha pygame e finaliza o programa
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #8. Alguma ação "por frame"
    
    #9. Limpa a janela        
    janela.fill(preto)
    
    #10. Desenha todos os elementos da janela
    # desenha a bola
    janela.blit(imagem_bola, (100,200))    
    #11. Atualiza a janela
    pygame.display.update()
    
    #12. Desacelera 
    #clock.tick(frames_por_segundo)