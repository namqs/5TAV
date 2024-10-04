# jogador_vs_jogador.py

from tabuleiro import mostrar_tabuleiro, inicializar_tabuleiro, jogada_valida, fazer_jogada, verificar_vencedor

def jogo_jogador_vs_jogador():
    tabuleiro = inicializar_tabuleiro()
    jogadores = ['X', 'O']
    turno = 0

    while tabuleiro[0] < 9:  # Até que o número de jogadas chegue a 9
        mostrar_tabuleiro(tabuleiro)
        jogador_atual = jogadores[turno % 2]
        print(f"Turno do jogador {jogador_atual}")
        
        try:
            posicao = int(input(f"Escolha uma posição de 1 a 9 para jogar: "))
            if posicao < 1 or posicao > 9 or not jogada_valida(tabuleiro, posicao):
                print("Posição inválida. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

        fazer_jogada(tabuleiro, jogador_atual, posicao)
        vencedor = verificar_vencedor(tabuleiro)
        
        if vencedor:
            mostrar_tabuleiro(tabuleiro)
            print(f"Jogador {vencedor} venceu!")
            return

        turno += 1

    print("Fim do jogo! Empate.")
    mostrar_tabuleiro(tabuleiro)

if __name__ == '__main__':
    jogo_jogador_vs_jogador()
