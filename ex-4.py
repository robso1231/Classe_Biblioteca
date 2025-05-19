class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} (Estoque: {self.estoque})"

class Carrinho:
    def __init__(self):
        self.itens = {}  # Dicionário para armazenar produtos e quantidades {produto: quantidade}
        self.cupom = None

    def adicionar_item(self, produto, quantidade=1):
        if produto in self.itens:
            self.itens[produto] += quantidade
        else:
            self.itens[produto] = quantidade
        produto.estoque -= quantidade
        print(f"{quantidade} unidade(s) de {produto.nome} adicionada(s) ao carrinho.")

    def remover_item(self, produto, quantidade=1):
        if produto in self.itens:
            if quantidade >= self.itens[produto]:
                del self.itens[produto]
                produto.estoque += self.itens[produto] # Devolve ao estoque a quantidade removida
                print(f"Todas as unidades de {produto.nome} foram removidas do carrinho.")
            else:
                self.itens[produto] -= quantidade
                produto.estoque += quantidade # Devolve ao estoque a quantidade removida
                print(f"{quantidade} unidade(s) de {produto.nome} removida(s) do carrinho.")
        else:
            print(f"{produto.nome} não está no carrinho.")

    def aplicar_cupom(self, cupom):
        self.cupom = cupom
        print(f"Cupom '{cupom.nome}' aplicado.")

    def listar_itens(self):
        if not self.itens:
            print("O carrinho está vazio.")
        else:
            print("Itens no carrinho:")
            for produto, quantidade in self.itens.items():
                print(f"- {produto.nome}: {quantidade} unidade(s)")

    def totalizar(self):
        total = sum(produto.preco * quantidade for produto, quantidade in self.itens.items())
        if self.cupom:
            if self.cupom.tipo == "porcentagem":
                total *= (1 - self.cupom.valor / 100)
            elif self.cupom.tipo == "fixo":
                total -= self.cupom.valor
                total = max(total, 0)
        return total

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.carrinho = Carrinho()

class Cupom:
    def __init__(self, nome, tipo, valor):
        self.nome = nome
        self.tipo = tipo
        self.valor = valor

# Produtos
p1 = Produto("Camisa", 100, 10)
p2 = Produto("Calça", 150, 5)
p3 = Produto("Sapato", 200, 3)

# Cliente
cliente = Cliente("João", "Rua A, 123")

# Cupons
cupom_10_porcento = Cupom("DESCONTO10", "porcentagem", 10)
cupom_50_reais = Cupom("50REAIS", "fixo", 50)

# Adicionando itens no carrinho
cliente.carrinho.adicionar_item(p1, 2)
cliente.carrinho.adicionar_item(p2)
cliente.carrinho.adicionar_item(p1)

# Listando carrinho
cliente.carrinho.listar_itens()

# Aplicando cupom
cliente.carrinho.aplicar_cupom(cupom_10_porcento)

# Total
print(f"Total a pagar após cupom: R${cliente.carrinho.totalizar():.2f}")

# Removendo um item do carrinho
cliente.carrinho.remover_item(p1)
cliente.carrinho.listar_itens()

# Aplicando outro cupom
cliente.carrinho.aplicar_cupom(cupom_50_reais)

# Total
print(f"Total a pagar após outro cupom: R${cliente.carrinho.totalizar():.2f}")

print(f"Total a pagar final: R${cliente.carrinho.totalizar():.2f}")