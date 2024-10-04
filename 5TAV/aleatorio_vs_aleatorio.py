from tabuleiro import mostrar_tabuleiro, inicializar_tabuleiro, jogada_valida, fazer_jogada, verificar_vencedor
import random

# Função para uma jogada aleatória
def jogada_aleatoria(tabuleiro):
    posicoes_disponiveis = [i for i in range(1, 10) if jogada_valida(tabuleiro, i)]
    return random.choice(posicoes_disponiveis)

# Função para simular um jogo aleatório vs aleatório
def jogo_aleatorio_vs_aleatorio():
    tabuleiro = inicializar_tabuleiro()
    jogadores = ['X', 'O']  # 'X' será o jogador que começa
    turno = 0

    while tabuleiro[0] < 9:
        jogador_atual = jogadores[turno % 2]
        posicao = jogada_aleatoria(tabuleiro)
        fazer_jogada(tabuleiro, jogador_atual, posicao)
        vencedor = verificar_vencedor(tabuleiro)

        if vencedor:
            return vencedor  # Retorna o jogador vencedor ('X' ou 'O')

        turno += 1

    return 'Empate'  # Retorna 'Empate' se ninguém vencer

# Função para rodar várias simulações
def simular_varios_jogos(num_jogos):
    vitorias_X = 0  # Contador de vitórias do primeiro jogador
    vitorias_O = 0  # Contador de vitórias do segundo jogador
    empates = 0     # Contador de empates

    for _ in range(num_jogos):
        vencedor = jogo_aleatorio_vs_aleatorio()
        if vencedor == 'X':
            vitorias_X += 1
        elif vencedor == 'O':
            vitorias_O += 1
        else:
            empates += 1

    # Exibir os resultados
    print(f"Jogos simulados: {num_jogos}")
    print(f"Vitórias do bot que começou (X): {vitorias_X}")
    print(f"Vitórias do bot que jogou em segundo (O): {vitorias_O}")
    print(f"Empates: {empates}")

# Main para rodar a simulação com número X de jogos
if __name__ == '__main__':
    numero_de_jogos = int(input("Quantos jogos você deseja simular? "))
    simular_varios_jogos(numero_de_jogos)
