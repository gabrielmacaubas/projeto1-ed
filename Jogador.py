from PilhaEncadeada import Pilha


class Jogador:

    def __init__(self, nome):
        self.__montante = None
        self.__nome = nome
        self.__quantidade = int()

    def receberCartas(self, baralho):
        self.__montante = Pilha()

        for i in range(26):
            self.__montante.empilha(baralho.retirarCarta())
            self.__quantidade += 1

    def quantidadeCartas(self):
        return self.__quantidade

    def imprime(self):
        print(f"Jogador {self.__nome}:", self.__str__())

    def getNome(self):
        return self.__nome

    def jogarCarta(self):
        self.__quantidade -= 1
        return self.__montante.desempilha()

    def __str__(self):
        return self.__montante
