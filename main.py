from Baralho import Baralho, BaralhoException
from PilhaEncadeada import Pilha, PilhaException
from Jogador import Jogador
from time import sleep

while True:
    # definição do jogo
    print("Início do jogo!")
    b = Baralho()
    cp = Pilha()
    j1 = Jogador(input("\nNome do 1º jogador: "))
    j2 = Jogador(input("Nome do 2º jogador: "))
    rodadas = int()

    # inicio do jogo
    for i in range(3):
        sleep(1)
        print(".")

    b.embaralhar()
    print("\nBaralho foi embaralhado!\n")

    sleep(1)
    j1.receberCartas(b)
    print(f"O jogador {j1.getNome()} recebeu {j1.quantidadeCartas()} cartas!")
    j2.receberCartas(b)
    print(f"O jogador {j2.getNome()} recebeu {j2.quantidadeCartas()} cartas!\n")

    # rodada
    sleep(2)
    print("O jogo será iniciado!!!")
    sleep(2)

    while j1.quantidadeCartas() != 0 and j2.quantidadeCartas() != 0 and rodadas < 100:
        rodadas += 1
        print(f"\n{rodadas}º rodada ->")
        
        while True:
            ganhador = str()
            carta1_valor = j1.topo().valor
            carta2_valor = j2.topo().valor

            cp.empilha(j1.jogarCarta())
            print(f"\nO jogador {j1.getNome()} jogou a carta {cp.topo()}")
            cp.empilha(j2.jogarCarta())
            print(f"O jogador {j2.getNome()} jogou a carta {cp.topo()}")

            if carta1_valor > carta2_valor:
                ganhador = j1.getNome()
                print(f"O jogador {ganhador} venceu e recebeu as cartas:", end=" ")
                cp.imprime()

                for i in range(cp.tamanho()):
                    j1.colocaBase(cp.desempilha())
                
                break

            elif carta2_valor > carta1_valor:
                ganhador = j2.getNome()
                print(f"O jogador {ganhador} venceu e recebeu as cartas:", end=" ")
                cp.imprime()    

                for i in range(cp.tamanho()):
                    j2.colocaBase(cp.desempilha()) 

                break
            
            print("Ops! Deu empate. Mais duas cartas na mesa!")
            continuar = input("Aperte [ENTER] para continuar")
                
        print(f"O jogador {j1.getNome()} agora tem {j1.quantidadeCartas()} cartas")
        print(f"O jogador {j2.getNome()} agora tem {j2.quantidadeCartas()} cartas")
        continuar = input("Aperte [ENTER] para continuar")
        

    #teste
    print()
    if j1.quantidadeCartas() > j2.quantidadeCartas():
        print(f"O jogador {j1.getNome()} ganhou o jogo!")
    
    elif j2.quantidadeCartas() > j1.quantidadeCartas(): 
        print(f"O jogador {j2.getNome()} ganhou o jogo!")
        
    
    else:
        print('Houve um empate!')

    reset = input("\nJogo encerrado. Deseja iniciar um novo jogo? (S/N)").upper()
    
    if reset == "N":
        break

print("Programa encerrado")
