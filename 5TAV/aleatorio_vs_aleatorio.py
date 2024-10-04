from tabuleiro import mostrar_tabuleiro, inicializar_tabuleiro, jogada_valida, fazer_jogada, verificar_vencedor
import random
import matplotlib.pyplot as plt

def jogada_aleatoria(tabuleiro):
    posicoes_disponiveis = [i for i in range(1, 10) if jogada_valida(tabuleiro, i)]
    return random.choice(posicoes_disponiveis)

def jogo_aleatorio_vs_aleatorio():
    tabuleiro = inicializar_tabuleiro()
    jogadores = ['X', 'O'] 
    turno = 0

    while tabuleiro[0] < 9:
        jogador_atual = jogadores[turno % 2]
        posicao = jogada_aleatoria(tabuleiro)
        fazer_jogada(tabuleiro, jogador_atual, posicao)
        vencedor = verificar_vencedor(tabuleiro)

        if vencedor:
            return vencedor  

        turno += 1

    return 'Empate'  

def gerar_grafico(num_jogos, vitorias_X, vitorias_O, empates):
    jogos = list(range(1, num_jogos + 1))

    plt.plot(jogos, vitorias_X, label="Vitórias X", color='blue', marker='o')
    plt.plot(jogos, vitorias_O, label="Vitórias O", color='red', marker='o')
    plt.plot(jogos, empates, label="Empates", color='green', marker='o')

    plt.xlabel("Número de Jogos")
    plt.ylabel("Vitórias/Empates")
    plt.title("Resultados ao Longo dos Jogos")
    plt.legend()

    plt.savefig('resultados_aleatorio_vs_aleatorio.png')
    plt.show()

def simular_varios_jogos(num_jogos):
    vitorias_X = 0  
    vitorias_O = 0 
    empates = 0  

    historico_vitorias_X = []
    historico_vitorias_O = []
    historico_empates = []

    for i in range(1, num_jogos + 1):
        vencedor = jogo_aleatorio_vs_aleatorio()
        if vencedor == 'X':
            vitorias_X += 1
        elif vencedor == 'O':
            vitorias_O += 1
        else:
            empates += 1

        historico_vitorias_X.append(vitorias_X)
        historico_vitorias_O.append(vitorias_O)
        historico_empates.append(empates)

    print(f"Jogos simulados: {num_jogos}")
    print(f"Vitórias do bot que começou (X): {vitorias_X}")
    print(f"Vitórias do bot que jogou em segundo (O): {vitorias_O}")
    print(f"Empates: {empates}")

    gerar_grafico(num_jogos, historico_vitorias_X, historico_vitorias_O, historico_empates)

if __name__ == '__main__':
    numero_de_jogos = int(input("Quantos jogos você deseja simular? "))
    simular_varios_jogos(numero_de_jogos)
