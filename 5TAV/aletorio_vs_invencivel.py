from tabuleiro import mostrar_tabuleiro, inicializar_tabuleiro, jogada_valida, fazer_jogada, verificar_vencedor 
import random
import matplotlib.pyplot as plt

def jogada_aleatoria(tabuleiro):
    posicoes_disponiveis = [i for i in range(1, 10) if jogada_valida(tabuleiro, i)]
    return random.choice(posicoes_disponiveis)

#invencivel
def melhor_jogada_computador(tabuleiro):
    #1° passo: ver se da pra vencer na proxima posição
    for i in range(1, 10):
        if jogada_valida(tabuleiro, i):
            tabuleiro[i] = -1 #simulação
            if verificar_vencedor(tabuleiro) == 'O':
                return i
            tabuleiro[i] = 0 

    #2° passo: verificar se o adversario vai vencer se ele colocar na proxima posição
    for i in range(1, 10):
        if jogada_valida(tabuleiro, i):
            tabuleiro[i] = 1 #simulação
            if verificar_vencedor(tabuleiro) == 'X':
                return i
            tabuleiro[i] = 0

    #3° passo: bota no centro
    if jogada_valida(tabuleiro, 5):
        return 5

    #4° passo: bota em um canto
    for i in [1, 3, 7, 9]:
        if jogada_valida(tabuleiro, i):
            return i

    #5° passo: bota em espaço livre
    for i in range(1, 10):
        if jogada_valida(tabuleiro, i):
            return i

def jogo_aleatorio_vs_invencivel():
    tabuleiro = inicializar_tabuleiro()
    jogadores = ['X', 'O'] #X é aleatorio e O é o invencivel
    turno = 0

    while tabuleiro[0] < 9:
        jogador_atual = jogadores[turno % 2]

        if jogador_atual == 'X': 
            posicao = jogada_aleatoria(tabuleiro)
        else:
            posicao = melhor_jogada_computador(tabuleiro)

        fazer_jogada(tabuleiro, jogador_atual, posicao)
        vencedor = verificar_vencedor(tabuleiro)

        if vencedor:
            return vencedor 

        turno += 1

    return 'Empate' 

def gerar_grafico(num_jogos, vitorias_aleatorio, vitorias_invencivel, empates):
    jogos = list(range(1, num_jogos + 1))

    plt.plot(jogos, vitorias_aleatorio, label="Vitórias Aleatório (X)", color='blue', marker='o')
    plt.plot(jogos, vitorias_invencivel, label="Vitórias Invencível (O)", color='red', marker='o')
    plt.plot(jogos, empates, label="Empates", color='green', marker='o')

    plt.xlabel("Número de Jogos")
    plt.ylabel("Vitórias/Empates")
    plt.title("Convergência dos Resultados ao Longo dos Jogos")
    plt.legend()

    plt.savefig('convergencia_resultados.png')
    plt.show()

def simular_varios_jogos(num_jogos):
    vitorias_invencivel = 0  
    vitorias_aleatorio = 0  
    empates = 0            

    historico_vitorias_aleatorio = []
    historico_vitorias_invencivel = []
    historico_empates = []

    for i in range(1, num_jogos + 1):
        vencedor = jogo_aleatorio_vs_invencivel()
        if vencedor == 'X':
            vitorias_aleatorio += 1
        elif vencedor == 'O':
            vitorias_invencivel += 1
        else:
            empates += 1

        historico_vitorias_aleatorio.append(vitorias_aleatorio)
        historico_vitorias_invencivel.append(vitorias_invencivel)
        historico_empates.append(empates)

    print(f"Jogos simulados: {num_jogos}")
    print(f"Vitórias do jogador aleatório (X): {vitorias_aleatorio}")
    print(f"Vitórias do jogador invencível (O): {vitorias_invencivel}")
    print(f"Empates: {empates}")


    gerar_grafico(num_jogos, historico_vitorias_aleatorio, historico_vitorias_invencivel, historico_empates)

if __name__ == '__main__':
    numero_de_jogos = int(input("Quantos jogos você deseja simular? "))
    simular_varios_jogos(numero_de_jogos)

