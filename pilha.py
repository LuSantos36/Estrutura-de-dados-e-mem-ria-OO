class Pilha:

    def __init__(self, max_size):
        self.max_size = max_size
        self.produto = []
    
    def push(self, produto):
        # Verifica se a pilha está cheia
        if len(self.produto) < self.max_size:
            self.produto.append(produto)
            print(f"Produto {produto} adicionado à pilha.")
        else:
            # Avisa que a pilha está cheia
            print(f"A pilha está cheia e não é possível adicionar mais produtos sem remover algum item.")  # Linha alterada
    
    def pop(self):
        if self.is_empty():
            print("A pilha está vazia. Não há item para remover.")
            return None
        else:
            return self.produto.pop()

    def peek(self):
        if self.is_empty():
            print("A pilha está vazia. Não há item para retornar.")
            return None
        else:
            return self.produto[-1]

    def is_empty(self):
        return len(self.produto) == 0  # pilha vazia

    def max_size(self):
        return self.max_size        # tamanho máximo

    def size(self):
        return len(self.produto)    # tamanho atual

    def print_stack(self):
        if self.is_empty():
            print("A pilha está vazia.")
        else:
            print("O estado atual da pilha:", self.produto)


def main():          
    max_size = int(input("Digite o tamanho máximo da pilha: "))
   
    # tamanho máximo definido pelo usuário
    pilha = Pilha(max_size)
    print(f"Tamanho máximo da pilha definido como {max_size}.")

    while True:
        print("\nEscolha uma operação:")
        print("1. Push (Adicionar produto)")
        print("2. Pop (Remover produto)")
        print("3. Peek (Ver topo)")
        print("4. Verificar se a pilha está vazia")
        print("5. O tamanho da pilha é: ")
        print("6. Sair")
       
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            produto = input("Digite o produto para adicionar: ")
            pilha.push(produto)
            pilha.print_stack()

        elif opcao == "2":
            removed_produto = pilha.pop()
            if removed_produto is not None:
                print(f"Produto removido: {removed_produto}")
            pilha.print_stack()

        elif opcao == "3":
            topo = pilha.peek()
            if topo is not None:
                print(f"Topo da pilha: {topo}")
            pilha.print_stack()

        elif opcao == "4":
            if pilha.is_empty():
                print("A pilha está vazia.")
            else:
                print("A pilha não está vazia.")
            pilha.print_stack()

        elif opcao == "5":
            print(f"O tamanho da pilha é {pilha.size()}")

        elif opcao == "6":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
