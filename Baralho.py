# Baralho = coleçao de cartas (lista de cartas)
from Carta import Carta
from PilhaEncadeada import Pilha
from random import sample

'''Classe para tratamento de erro'''
class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Baralho:
    def __init__(self):

        '''Definição inicial do baralho como uma Pilha (estrutura pedida para o projeto), com naipe, numeração, e o valor atribuído a cada numeração a partir de um dicionário.'''
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

        '''For utilizado para atribuir as informações anteriores a uma lista só, a partir do length do naipe, e da numeração'''
        for idx in range(len(self.naipe)):
            for id in self.numeracao:
                self.baralho_original.append(Carta(id, self.naipe[idx], self.valores[id]))

    '''Método para determinar o tamanho do baralho.'''
    def __len__(self):
        return self.__baralho.tamanho()

    '''Método que identifica se o baralho está vazio.'''
    def temCarta(self):
        if not self.__baralho.estaVazia():
            return True

        return False

    '''Método que retira carta do baralho'''
    def retirarCarta(self) -> Carta:
        if not self.temCarta():
            raise BaralhoException("O baralho está vazio")
        
        else:
            return self.__baralho.desempilha()   

    '''Método para embaralhar o baralho'''
    def embaralhar(self):
        '''Cria baralho embaralhado temporário usando sample ao invés de shuffle para manter o self.baralho_original intacto.'''
        baralho_embaralhado = sample(self.baralho_original, 52)

        '''Começa a empilhar as cartas do baralho embaralhado no baralho padrão que é uma pilha encadeada.'''
        for c in baralho_embaralhado:
            self.__baralho.empilha(c)

    '''Método para imprimir todos os elementos do baralho, desde o topo até a base.'''
    def imprime(self):
        print("Baralho: topo->", self.__str__(), "<-base")

    '''Método que transforma o objeto em string.'''
    def __str__(self):
        return self.__baralho
