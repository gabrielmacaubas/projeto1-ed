from Baralho import Baralho, BaralhoException
from PilhaEncadeada import Pilha, PilhaException
from Jogador import Jogador

# definição do jogo
b = Baralho()
cp = Pilha()
j1 = Jogador("Cabras")
j2 = Jogador("Vitorianas")

# inicio do jogo
b.embaralhar()
print("Baralho foi embaralhado!\n")
j1.receberCartas(b)
print(f"O jogador {j1.getNome()} recebeu {j1.quantidadeCartas()} cartas!")
j2.receberCartas(b)
print(f"O jogador {j2.getNome()} recebeu {j2.quantidadeCartas()} cartas!\n")

# rodada
cp.empilha(j1.jogarCarta())
print(f"O jogador {j1.getNome()} jogou a carta {cp.topo()}")
cp.empilha(j2.jogarCarta())
print(f"O jogador {j2.getNome()} jogou a carta {cp.topo()}")
print(f"O jogador {j1.getNome()} venceu recebeu as cartas:", end=" ")
cp.imprime()
for i in range(cp.tamanho()):
    j1.colocaBase(cp.desempilha())

#teste
print()
j1.imprime()
j2.imprime()
