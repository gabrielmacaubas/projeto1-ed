from Baralho import Baralho, BaralhoException
from PilhaEncadeada import Pilha, PilhaException
from Jogador import Jogador, JogadorException
from time import sleep

# while de todos os jogos
while True:
    # Definição do jogo
    print("Início do jogo!")
    b = Baralho()
    cp = Pilha()
    j1 = Jogador(input("\nNome do(a) 1º jogador(a): "))
    j2 = Jogador(input("Nome do(a) 2º jogador(a): "))
    rodadas = int()
    rodadas_max = 100

    # Variáveis de cores
    lines = "=" * 35
    vermelho = '\033[91m'
    verde = '\033[92m'
    amarelo = '\033[93m'
    negrito = '\033[1m'
    stop = '\033[m'

    # inicio do jogo
    print(lines)
    print("\nO baralho está embaralhando...\n")
    print(lines)
    sleep(0.5)
    b.embaralhar()
    print("\nBaralho foi embaralhado!\n")
    print(lines)

    sleep(1)

    # Os 2 jogadores recebem suas 26 cartas
    try:
        j1.receberCartas(b)
        print(f"O(a) jogador(a) {j1.getNome()} recebeu {len(j1)} cartas!")
        j2.receberCartas(b)
        print(f"O(a) jogador(a) {j2.getNome()} recebeu {len(j2)} cartas!\n")
    except BaralhoException as be:
        print(be)
    
    sleep(1)
    print("O jogo será iniciado!!!")
    sleep(1)

    # while de cada jogo
    while len(j1) != 0 and len(j2) != 0 and rodadas < rodadas_max:
        rodadas += 1
        print(f"\n{negrito}{rodadas}ª rodada de {rodadas_max}->{stop}")
        
        # while de cada rodada
        while True:
            ganhador = str()
            carta1_valor = j1.topo().valor
            carta2_valor = j2.topo().valor

            sleep(0.1)

            # começo da rodada em que os jogadores jogam suas cartas do topo
            try:
                cp.empilha(j1.jogarCarta())
                print(f"\nO(a) jogador(a) {j1.getNome()} jogou a carta {cp.topo()}")
                sleep(0.1)
                cp.empilha(j2.jogarCarta())
                print(f"O(a) jogador(a) {j2.getNome()} jogou a carta {cp.topo()}")
            except JogadorException as je:
                print(je)

            try:
                # testar se uma carta é maior que a outra
                if carta1_valor > carta2_valor:
                    ganhador = j1.getNome()
                    sleep(0.1)
                    print(f"{amarelo}O(a) jogador(a) {ganhador} venceu e recebeu as cartas:", end=" ")
                    cp.imprime()
                    print(stop)

                    # jogador vencedor da rodada recebendo as cartas da pilha
                    for i in range(cp.tamanho()):
                        j1.inserirBase(cp.desempilha())
                    
                    break

                # testar se uma carta é maior que a outra
                elif carta2_valor > carta1_valor:
                    ganhador = j2.getNome()
                    sleep(0.1)
                    print(f"{amarelo}O(a) jogador(a) {ganhador} venceu e recebeu as cartas:", end=" ")
                    cp.imprime()
                    print(stop)

                    # jogador vencedor da rodada recebendo as cartas da pilha
                    for i in range(cp.tamanho()):
                        j2.inserirBase(cp.desempilha()) 

                    break
            except PilhaException as pe:
                print(pe)

            # Situação de empate na rodada
            print(f"{vermelho}Ops! Deu empate. Mais duas cartas na mesa!{stop}")
            continuar = input("Aperte [ENTER] para continuar")

        sleep(0.1)        
        print(f"O(a) jogador(a) {j1.getNome()} agora tem {len(j1)} cartas")
        print(f"O(a) jogador(a) {j2.getNome()} agora tem {len(j2)} cartas")
        continuar = input("Aperte [ENTER] para continuar")
        

    # teste para definir vencedor do jogo
    print()
    if len(j1) > len(j2):
        print(f"{verde}{lines}")
        print(f"O(a) jogador(a) {j1.getNome()} ganhou o jogo!")
        print(f"{lines}{stop}")

    elif len(j2) > len(j1): 
        print(f"{verde}{lines}")
        print(f"O(a) jogador(a) {j2.getNome()} ganhou o jogo!")
        print(f"{lines}{stop}")
        
    # situação de empate ao fim da partida
    else:
        print('Houve um empate!')

    # teste para saber se o usuário quer jogar mais um jogo
    reset = input("\nJogo encerrado. Deseja iniciar um novo jogo? (S/N) ").upper()
    
    if reset == "N":
        break

print("Programa encerrado")
