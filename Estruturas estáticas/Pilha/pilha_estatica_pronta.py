class Pilha:
    def __init__(self):
        self.itens = []

    #Funcao empilha
    def push(self, item):
        self.itens.append(item)

    # Funcao vazia
    def empty(self):
        return len(self.itens) == 0
    
    # Funcao desempilha
    def pop(self):
        assert not self.empty(), 'A pilha está vazia'
        return self.itens.pop()
    
def main():
    
    # Criando a instancia da pilha
    minha_pilha = Pilha()

    minha_pilha.push(10)
    minha_pilha.push(15)
    minha_pilha.push(20)
    minha_pilha.push(25)
    minha_pilha.push(30)

    print(minha_pilha.itens)

    minha_pilha.pop()
    minha_pilha.pop()

    print(minha_pilha.itens)

if __name__ == "__main__":
    main()
    