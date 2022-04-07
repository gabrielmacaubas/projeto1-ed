from Baralho import Baralho, BaralhoException
from PilhaEncadeada import Pilha, PilhaException
from Jogador import Jogador

b = Baralho()
cp = Pilha()
j1 = Jogador("Cabras")
j2 = Jogador("Vitorianas")

b.embaralhar()
print("Baralho foi embaralhado!\n")
j1.receberCartas(b)
print(f"O jogador {j1.getNome()} recebeu {j1.quantidadeCartas()} cartas!\n")
j2.receberCartas(b)
print(f"O jogador {j2.getNome()} recebeu {j2.quantidadeCartas()} cartas!\n")


cp.empilha(j1.jogarCarta())
print(f"O jogador {j1.getNome()} jogou a carta {cp.topo()}")
cp.empilha(j2.jogarCarta())
print(f"O jogador {j2.getNome()} jogou a carta {cp.topo()}")
