# Implementacao de uma arvore binaria utilizando uma pilha para realizar o caminhamento PRE-ORDEM

# Classe que representa cada noh, com o valor de referencia para os filhos esquerdo e direito
class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

# Classe para gerenciar a arvore em si
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        # Insere na sub arvore esquerda
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        # Insere na sub arvore direita
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)
    
    def preorder(self, root):
        if root:
            # cria a instancia da pilha
            pilha = Stack()

            # 1. Empilhar a raiz
            pilha.push(root)

            # 2. Repetir ate que a pilha fique vazia
            while not pilha.empty():
                # 2.1 Desempilha o topo da pilha (visita)
                no_atual = pilha.pop()
                print(no_atual.value, end=' ')

                # 2.2 Empilha noh da esquerda se diferente de NULL
                if no_atual.left is not None:
                    pilha.push(no_atual.left)
                # 2.3 Empilha noh da diretia se diferente de NULL
                if no_atual.right is not None:
                    pilha.push(no_atual.right)

# Classe que representa a pilha
class Stack:
    def __init__(self):
        self.itens = []

    # Funcao empilha
    def push(self, item):
        self.itens.append(item)

    # Funcao vazia
    def empty(self):
        return len(self.itens) == 0
    
    # Funcao desempilha
    def pop(self):
        if self.empty():
            raise IndexError("A pilha esta vazia")
        else:
            return self.itens.pop()

if __name__ == "__main__":
    tree = BinaryTree()
    elements = [27, 14, 35, 10, 19, 31, 42]

    for elem in elements:
        tree.insert(elem)

    print("Percurso em pre-ordem: ")
    tree.preorder(tree.root)
