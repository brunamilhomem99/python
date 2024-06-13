from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def __len__(self):
        # Retorna o tamanho da lista
        return self._size
    
    # Funcao empilha
    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    # Funcao desempilha
    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node
        else:
            raise IndexError("A pilha está vazia!")

    # Retorna o topo da pilha sem remover
    def peek(self):
        if self._size > 0:
            return self.top.data
        else:
            raise IndexError("A pilha está vazia!")
        
    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()

def main():
     
    minha_pilha = Stack()

    minha_pilha.push(10)
    minha_pilha.push(15)
    minha_pilha.push(20)
    minha_pilha.push(25)
    minha_pilha.push(30)

    print(minha_pilha)

    minha_pilha.pop()
    minha_pilha.pop()

    print(minha_pilha)

if __name__ == "__main__":
    main()
