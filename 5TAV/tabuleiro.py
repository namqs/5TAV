import random

def mostrar_tabuleiro(tabuleiro):
    def simbolo(pos):
        if tabuleiro[pos] == 1:
            return 'X'
        elif tabuleiro[pos] == -1:
            return 'O'
        else:
            return str(pos)

    print(f"{simbolo(1)} | {simbolo(2)} | {simbolo(3)}")
    print("--+---+--")
    print(f"{simbolo(4)} | {simbolo(5)} | {simbolo(6)}")
    print("--+---+--")
    print(f"{simbolo(7)} | {simbolo(8)} | {simbolo(9)}")

def inicializar_tabuleiro():
    return [0] * 10  #array com 10 posições

def jogada_valida(tabuleiro, posicao):
    return tabuleiro[posicao] == 0

def fazer_jogada(tabuleiro, jogador, posicao):
    if jogador == 'X':
        tabuleiro[posicao] = 1
    elif jogador == 'O':
        tabuleiro[posicao] = -1
    tabuleiro[0] += 1 #contador de jogadas

def verificar_vencedor(tabuleiro):
    combinacoes_vencedoras = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9],  [1, 5, 9], [3, 5, 7]            
    ]
    
    for combinacao in combinacoes_vencedoras:
        soma = tabuleiro[combinacao[0]] + tabuleiro[combinacao[1]] + tabuleiro[combinacao[2]]
        if soma == 3:
            return 'X'
        elif soma == -3:
            return 'O'
    return None

def jogar_automatico(tabuleiro):
    posicoes_disponiveis = [i for i in range(1, 10) if jogada_valida(tabuleiro, i)]
    return random.choice(posicoes_disponiveis)
