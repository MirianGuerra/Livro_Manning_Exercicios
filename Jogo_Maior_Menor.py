"""Jogo Maior ou Menor"""
"""
Nesse jogo 8 cartas são escolhidas aleatoriamente de um deck. 
A primeira carta é mostrada e o jogador deve predizer se a proxima carta é maior ou menor do que a da mesa.
Se acertar ganha 20 pontos
Se errar perde 15 pontos
Se for iguar perde.
"""

import numpy as np
import sys # importação aqui


def cria_baralho():
    baralho_completo = {'As':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Dama':11,'Valete':12, 'Rei':13}
    return baralho_completo

def escolhendo_8_cartas():
    baralho_completo = cria_baralho()
    valores_aleatorios = np.random.randint(1,14,8)
    cartas = [i for i in baralho_completo.keys()]
    #valores = [i for i in baralho_completo.values()]
    cartas_aleatorias = [cartas[i-1] for i in valores_aleatorios]
    return cartas_aleatorias, valores_aleatorios

def virando_primeira_carta():
    cartas_aleatorias, valores_aleatorias = escolhendo_8_cartas()
    primeira_carta = cartas_aleatorias[0]
    primeiro_valor = valores_aleatorias[0]
    print(f'**********************\n A Carta virada é: \n ******** {primeira_carta} ********\n**********************')
    return primeiro_valor
    
def escolha_jogador():
    escolha = input("A próxima carta será MAIOR ou MENOR? ")
    escolha = escolha.upper()
    return escolha

print('******** JOGO MAIOR OU MENOR ********')
print('\n\n******** Regras ********\n\n-Começa o jogo com 0 pontos.\n-Após a primeira carta escolha se a próxima será MAIOR ou MENOR do que a carta virada.')
print('-Se acertar ganha 20 pontos.\n-Se errar perde 15 pontos.\n-O jogo termina se ficar com menos de 0 pontos.\n************************************************\n')

primeiro_valor = virando_primeira_carta()
pontuacao = 0
i=1
cartas_aleatorias, valores_aleatorios = escolhendo_8_cartas()
for i in range(0,8):
    escolha = escolha_jogador()
    if escolha == "MAIOR":
        if valores_aleatorios[i]>primeiro_valor:
            pontuacao = pontuacao + 20
            print("\nVoce acertou!!")
            print(f'Pontuação: {pontuacao}')
            primeiro_valor=valores_aleatorios[i]
        else:
            pontuacao = pontuacao-15
            print('\nVoce Errou!!')
            print(f'Pontuação: {pontuacao}')
            primeiro_valor=valores_aleatorios[i]
        

    if escolha == "MENOR":
        if valores_aleatorios[i]<primeiro_valor:
            pontuacao = pontuacao+20
            print("\nVoce acertou!!")
            print(f'Pontuação: {pontuacao}')
            primeiro_valor=valores_aleatorios[i]

        else:
            pontuacao = pontuacao-15
            print('\nVoce Errou!!')
            print(f'Pontuação: {pontuacao}')
            primeiro_valor=valores_aleatorios[i]
            
    if pontuacao < 0:
        sys.exit("\nVoce perdeu! =(")
 
    print(f'**********************\n A Carta virada é: \n ******** {cartas_aleatorias[i]} ********\n**********************')
    
print('************* Parabéns! *************')
print('************ Voce Ganhou! ************')
print(f'*** Sua pontuação foi de {pontuacao} pontos ***')
