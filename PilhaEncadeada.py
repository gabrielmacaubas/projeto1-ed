# Classe para tratamento de erros
class PilhaException(Exception):

    def __init__(self, mensagem, metodo=''):
        super().__init__(mensagem)

        self.metodo = metodo


# Classe para criar cada nó da pilha encadeada
class Node:

    # Método construtor da classe Nó
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

    """Método que insere o próximo dado. Se não houver nenhum dado na posição de próximo, 
    o dado vai ser inserido nessa posição."""
    def insereProximo(self, dado):
        if self.prox is None:
            self.prox = Node(dado)

    # Método que retorna o próximo elemento do nó atual
    def getProximo(self):
        return self.prox

    # Método que retorna a string do nó
    def __str__(self):
        return str(self.data)

    # Método que verifica se há um próximo nó
    def temProximo(self):
        return self.prox is not None


# Classe para criar objetos do tipo Pilha encadeada.
class Pilha:

    # Método construtor da classe Pilha
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    # Método que verifica se a pilha está vazia
    def estaVazia(self):
        return self.__head is None

    # Método que retorna o tamanho da pilha
    def tamanho(self):
        return self.__tamanho

    # Método que retorna o elemento do topo da pilha
    def topo(self):
        return self.__head.dado

    # Método que determina, a partir de uma posição, o elemento localizado nela.
    def elemento(self, posicao):
        try:
            assert 0 < posicao <= self.__tamanho

            cursor = self.__head
            contador = 1

            while cursor is not None and contador < posicao:
                contador += 1
                cursor = cursor.prox

            return cursor.dado

        except TypeError:
            raise PilhaException('Digite um número inteiro referente ao elemento desejado')
        except AssertionError:
            raise PilhaException(f'O elemento {posicao} NAO existe na pilha de tamanho {self.__tamanho}')
        except:
            raise

    # Método que retorna a posição a partir do valor informado.
    def busca(self, valor):
        cursor = self.__head
        contador = 1

        while cursor is not None:
            if cursor.dado == valor:
                return contador
            cursor = cursor.prox
            contador += 1

        raise PilhaException(f'Valor {valor} nao esta na pilha', 'busca()')

    # Método que empilha o dado.
    def empilha(self, valor):
        novo = Node(valor)
        novo.prox = self.__head

        self.__head = novo
        self.__tamanho += 1

    # Método que quebra o conceito de pilha para empilhar na base da mesma.
    def empilhaBase(self, valor):
        novo = Node(valor)

        """Caso a pilha esteja vazia, o valor será inserido no topo, caso não esteja vazia, 
        este método irá passar por todos os nós até encontrar um que não tenha um valor no próximo, 
        ou seja, o último nó."""
        if self.estaVazia():
            self.__head = novo
            return
        else:
            temp = self.__head
            while temp.prox is not None:
                temp = temp.prox
            temp.prox = novo

        self.__tamanho += 1

    # Método que desempilha um elemento da pilha.
    def desempilha(self):

        """Primeiro, há de se verificar se  pilha não está vazia. Neste caso,
        o topo passa a ser o próximo e o tamanho é reduzido em 1."""
        if not self.estaVazia():
            dado = self.__head.dado

            self.__head = self.__head.prox
            self.__tamanho -= 1

            return dado
        raise PilhaException('A pilha está vazia')

    # Método para imprimir o código.
    def imprime(self):
        print(self.__str__())

    # Método que transforma objeto em string.
    def __str__(self):
        cursor = self.__head
        primeiro = True
        s = '['

        while cursor is not None:
            if primeiro:
                s += f'{cursor.dado}'
                primeiro = False

            else:
                s += f', {cursor.dado}'

            cursor = cursor.prox

        s += ']'
        return s
