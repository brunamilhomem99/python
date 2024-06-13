# Implementacao de uma arvore binaria utilizando uma fila para realizar o caminhamento em LARGURA

import queue

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
    
    def level(self, root):
        if root:
            # Inicializa a fila
            fila = queue.Queue()

            # 1. Adicionar a raiz na fila
            fila.put(root)

            # 2. Repetir ate que a fila fique vazia
            while not fila.empty():
                # 2.1 Retirar o primeiro elemento da pilha (visita)
                no_atual = fila.get()
                print(no_atual.value, end=' ')

                # 2.2 Adiciona noh da esquerda se diferente de NULL
                if no_atual.left is not None:
                    fila.put(no_atual.left)
                # 2.3 Adiciona noh da diretia se diferente de NULL
                if no_atual.right is not None:
                    fila.put(no_atual.right)


if __name__ == "__main__":
    tree = BinaryTree()
    elements = [27, 14, 35, 10, 19, 31, 42]

    for elem in elements:
        tree.insert(elem)

    print("Percurso em largura: ")
    tree.level(tree.root)