class Carta:

    def __init__(self, numero, naipe, valor):
        self.__numero = numero
        self.__naipe = naipe
        self.__valor = valor

    @property
    def naipe(self):
        return self.__naipe

    @property
    def numero(self):
        return self.__numero

    @property
    def valor(self):
        return self.__valor

    def __str__(self): # todas as informacoes da carta
        return f'{self.__numero} de {self.__naipe}'
