# Baralho = coleçao de cartas (lista de cartas)
from Carta import Carta
from PilhaEncadeada import Pilha
from random import sample


class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Baralho:
    def __init__(self):
        self.Baralho = Pilha()

        self.baralho_original = list()
        naipe = ["Ouro", "Espada", "Paus", "Copas"]
        numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]

        for idx in range(len(naipe)):
            for id in numeracao:
                self.baralho_original.append(Carta(id, naipe[idx]))

    def __len__(self):
        return self.Baralho.tamanho()

    def temCarta(self):
        if not self.Baralho.estaVazia():
            return True

        return False

    def retirarCarta(self) -> Carta:
        return self.Baralho.desempilha()

    def embaralhar(self):
        baralho_embaralhado = sample(self.baralho_original, 52)
        self.Baralho.empilhaSerie(baralho_embaralhado)

    def imprime(self):
        print(self.Baralho)


if __name__ == "__main__":
    b = Baralho()
    print("tem carta?", b.temCarta())
    b.embaralhar()
    b.imprime()
    print("tem carta?", b.temCarta())
    for i in range(52):
        print(f'{b.retirarCarta()} foi desempilhado!')
    print("tem carta?", b.temCarta())
    b.imprime()
