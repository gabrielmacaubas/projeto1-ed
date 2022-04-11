# Baralho = coleçao de cartas (lista de cartas)
from Carta import Carta
from PilhaEncadeada import Pilha
from random import sample


class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Baralho:
    def __init__(self):
        self.__baralho = Pilha()

        self.baralho_original = list()
        self.naipe = ["Ouro", "Espada", "Paus", "Copas"]
        self.numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]
        self.valores = {
            'As': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'valete': 11,
            'dama': 12,
            'rei': 13
        }
        for idx in range(len(self.naipe)):
            for id in self.numeracao:
                self.baralho_original.append(Carta(id, self.naipe[idx], self.valores[id]))

    def __len__(self):
        return self.__baralho.tamanho()

    def temCarta(self):
        if not self.__baralho.estaVazia():
            return True

        return False

    def retirarCarta(self) -> Carta:
        return self.__baralho.desempilha()

    def embaralhar(self):
        baralho_embaralhado = sample(self.baralho_original, 52)

        for c in baralho_embaralhado:
            self.__baralho.empilha(c)

    def imprime(self):
        print("Baralho: topo->", self.__str__(), "<-base")

    def __str__(self):
        return self.__baralho
