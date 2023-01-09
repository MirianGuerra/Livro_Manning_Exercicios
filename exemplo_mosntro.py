import random
import math

class Monstro():
    def __init__(self, nro_colunas:int, nro_linhas:int, velocidade_maxima:int) -> None:
        self.nro_colunas = nro_colunas
        self.nro_linhas = nro_linhas
        self.minha_linha = random.randrange(self.nro_linhas)
        self.minha_coluna = random.randrange(self.nro_colunas)
        self.minha_velocidade_x = random.randrange(-velocidade_maxima, velocidade_maxima+1)
        self.minha_velocidade_y = random.randrange(-velocidade_maxima, velocidade_maxima+1)
        
    def mover(self):
        self.minha_linha = (self.minha_linha + self.minha_velocidade_y)%self.nro_linhas
        self.minha_coluna = (self.minha_coluna +self.minha_velocidade_x) % self.nro_colunas
        
    def mostrar(self):
        print(f'Posição {self.minha_linha}x{self.minha_coluna}')
        print(f'Velocidade {round(math.sqrt(self.minha_velocidade_x**2+self.minha_velocidade_y**2),1)}')
        print('')


nro_monstros = 20
nro_linhas = 100
nro_colunas = 100
velocidade_maxima = 4
lista_monstros = []
for i in range(nro_monstros):
    monstro = Monstro(nro_colunas, nro_linhas, velocidade_maxima)
    lista_monstros.append(monstro)
    monstro.mostrar()