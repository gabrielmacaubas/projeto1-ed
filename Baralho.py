# Baralho = coleçao de cartas (lista de cartas)
from Carta import Carta
from PilhaEncadeada import Pilha
from random import shuffle


# Classe para tratamento de erro
class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Baralho:

    def __init__(self):
        """Definição inicial do baralho como uma Pilha (estrutura
        pedida para o projeto), com naipe, numeração, e o valor 
        atribuído a cada numeração a partir de um dicionário."""
        baralho = list()
        naipe = ["Ouro", "Espada", "Paus", "Copas"]
        numeracao = {
            'As': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'valete': 11,
            'dama': 12, 'rei': 13
        }

        """For utilizado para atribuir as informações anteriores a 
        uma lista só, a partir do length do naipe, e da 
        numeração"""
        for idx in range(len(naipe)):
            for chave, valor in numeracao.items():
                baralho.append(Carta(chave, naipe[idx], valor))
        
        """Atribuição de todas as cartas do baralho em uma pilha 
        para uma pilha encadeada"""
        self.__baralho = Pilha()
        for c in baralho:
            self.__baralho.empilha(c)

    # Método para determinar o tamanho do baralho.
    def __len__(self):
        return self.__baralho.tamanho()

    # Método que identifica se o baralho está vazio.
    def temCarta(self):
        if not self.__baralho.estaVazia():
            return True

        return False

    # Método que retira carta do baralho
    def retirarCarta(self) -> Carta:
        if not self.temCarta():
            raise BaralhoException("O baralho está vazio")
        
        else:
            return self.__baralho.desempilha()   

    # Método para embaralhar o baralho
    def embaralhar(self):
        """Cria baralho temporário onde é usado a função shuffle
        da biblioteca random"""
        baralho_temp = list()
        for i in range(self.__baralho.tamanho()):
            baralho_temp.append(self.__baralho.desempilha())
        
        """Começa a empilhar as cartas do baralho temporário já 
        embaralhadas no baralho padrão que é uma pilha encadeada"""
        shuffle(baralho_temp)
        for c in baralho_temp:
            self.__baralho.empilha(c)

    """Método para imprimir todos os elementos do baralho, desde o 
    topo até a base."""
    def imprime(self):
        print("Baralho: topo->", self.__str__(), "<-base")

    # Método que transforma o objeto em string.
    def __str__(self):
        return self.__baralho
