from Baralho import Baralho, BaralhoException
from PilhaEncadeada import Pilha, PilhaException
from Jogador import Jogador, JogadorException
from time import sleep

'''while de todos os jogos'''
while True:
    '''Definição do jogo'''
    print("Início do jogo!")
    b = Baralho()
    cp = Pilha()
    j1 = Jogador(input("\nNome do(a) 1º jogador(a): "))
    j2 = Jogador(input("Nome do(a) 2º jogador(a): "))
    rodadas = int()
    lines = "=" * 30

    '''inicio do jogo'''
    print(lines)
    print("\nO baralho está embaralhando...\n")
    print(lines)
    sleep(0.5)
    b.embaralhar()
    print("\nBaralho foi embaralhado!\n")
    print(lines)

    sleep(1)

    '''Os 2 jogadores recebem suas 26 cartas'''
    try:
        j1.receberCartas(b)
        print(f"O(a) jogador(a) {j1.getNome()} recebeu {j1.quantidadeCartas()} cartas!")
        j2.receberCartas(b)
        print(f"O(a) jogador(a) {j2.getNome()} recebeu {j2.quantidadeCartas()} cartas!\n")
    except BaralhoException as be:
        print(be)
    
    sleep(1)
    print("O jogo será iniciado!!!")
    sleep(1)

    '''while de cada jogo'''
    while j1.quantidadeCartas() != 0 and j2.quantidadeCartas() != 0 and rodadas < 100:
        rodadas += 1
        print(f"\n{rodadas}ª rodada ->")
        
        '''while de cada rodada'''
        while True:
            ganhador = str()
            carta1_valor = j1.topo().valor
            carta2_valor = j2.topo().valor

            sleep(0.1)

            '''começo da rodada em que os jogadores jogam suas cartas do topo'''
            try:
                cp.empilha(j1.jogarCarta())
                print(f"\nO(a) jogador(a) {j1.getNome()} jogou a carta {cp.topo()}")
                sleep(0.1)
                cp.empilha(j2.jogarCarta())
                print(f"O(a) jogador(a) {j2.getNome()} jogou a carta {cp.topo()}")
            except JogadorException as je:
                print(je)

            '''testar se uma carta é maior que a outra'''
            try:
                if carta1_valor > carta2_valor:
                    ganhador = j1.getNome()
                    sleep(0.1)
                    print(f"O(a) jogador(a) {ganhador} venceu e recebeu as cartas:", end=" ")
                    cp.imprime()
                    
                    for i in range(cp.tamanho()):
                        j1.colocaBase(cp.desempilha())
                    
                    break

                elif carta2_valor > carta1_valor:
                    ganhador = j2.getNome()
                    sleep(0.1)
                    print(f"O(a) jogador(a) {ganhador} venceu e recebeu as cartas:", end=" ")
                    cp.imprime()    

                    for i in range(cp.tamanho()):
                        j2.colocaBase(cp.desempilha()) 

                    break
            except PilhaException as pe:
                print(pe)
            
            print("Ops! Deu empate. Mais duas cartas na mesa!")
            continuar = input("Aperte [ENTER] para continuar")

        sleep(0.1)        
        print(f"O(a) jogador(a) {j1.getNome()} agora tem {j1.quantidadeCartas()} cartas")
        print(f"O(a) jogador(a) {j2.getNome()} agora tem {j2.quantidadeCartas()} cartas")
        continuar = input("Aperte [ENTER] para continuar")
        

    '''teste para definir vencedor do jogo'''
    print()
    if j1.quantidadeCartas() > j2.quantidadeCartas():
        print(f"O jogador {j1.getNome()} ganhou o jogo!")
    
    elif j2.quantidadeCartas() > j1.quantidadeCartas(): 
        print(f"O jogador {j2.getNome()} ganhou o jogo!")
        
    
    else:
        print('Houve um empate!')

    '''teste para saber se o usuário quer jogar mais um jogo'''
    reset = input("\nJogo encerrado. Deseja iniciar um novo jogo? (S/N)").upper()
    
    if reset == "N":
        break

print("Programa encerrado")
