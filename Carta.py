'''Criação da classe carta'''
class Carta:
    '''método construtor da carta'''
    def __init__(self, numero, naipe, valor):
        self.__numero = numero
        self.__naipe = naipe
        self.__valor = valor

    '''Método de acesso ao naipe da carta'''
    @property
    def naipe(self):
        return self.__naipe

    '''Método de acesso a numeração da carta'''
    @property
    def numero(self):
        return self.__numero

    '''Método de acesso ao valor da carta'''
    @property
    def valor(self):
        return self.__valor

    '''Método que exibe cada carta junto de seu naipe'''
    def __str__(self): 
        return f'{self.__numero} de {self.__naipe}'
