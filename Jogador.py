from PilhaEncadeada import Pilha


# Classe para tratamento de erro
class JogadorException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Jogador:

    # Método construtor de Jogador
    def __init__(self, nome):
        self.__montante = Pilha()
        self.__nome = nome
        self.__quantidade = int()

    # Método que retorna o tamanho do montante
    def __len__(self):
        return self.__montante.tamanho()

    # Método para recebimento de cartas
    def receberCartas(self, baralho):
        self.__montante = Pilha()

        for i in range(26):
            self.__montante.empilha(baralho.retirarCarta())
            self.__quantidade += 1

    # Método para retornar a quantidade de cartas
    def quantidadeCartas(self):
        return self.__quantidade
    
    # Método que confere se o montante do jogador está vazio
    def esta_vazia(self):
        if self.quantidadeCartas() == 0:
            return True
        return False

    # Método que retorna o nome do jogador
    def getNome(self):
        return self.__nome

    # Método para tirar carta do topo do montante do jogador
    def jogarCarta(self):
        if self.esta_vazia():
            raise JogadorException(f"A pilha do jogador {self.getNome} está vazia.")

        else:
            self.__quantidade -= 1
            return self.__montante.desempilha()

    """Método que desempilha as cartas do campo de batalha, e 
    empilha na base do baralho do jogador"""
    def inserirBase(self, carta):
        self.__montante.empilhaBase(carta)
        self.__quantidade += 1
        
    # Método que retorna o topo do montante do Jogador
    def topo(self):
        return self.__montante.topo()

    # Método que imprime o montante do Jogador
    def imprime(self):
        print(f"Jogador {self.__nome}: topo->", self.__str__(), "<-base")

    # Método que retorna a string do montante
    def __str__(self):
        return self.__montante
