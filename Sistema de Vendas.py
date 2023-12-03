class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto, quantidade):
        self.produtos.append({'produto': produto, 'quantidade': quantidade})

    def calcular_total(self):
        total = 0
        for item in self.produtos:
            total += item['produto'].preco * item['quantidade']
        return total

class Carrinho:
    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

class Venda:
    def __init__(self, carrinho):
        self.carrinho = carrinho

    def fechar_venda(self):
        total_venda = 0
        for pedido in self.carrinho.pedidos:
            total_venda += pedido.calcular_total()
        return total_venda

class Relatorio:
    def gerar_relatorio(self, venda):
        print("Relatório de Venda:")
        print(f"Total da venda: R${venda.fechar_venda():.2f}")

# Exemplo de Uso com Inputs do Usuário
produto_nome1 = input("Digite o nome do Produto A: ")
produto_preco1 = float(input("Digite o preço do Produto A: "))
produto1 = Produto(produto_nome1, produto_preco1)

produto_nome2 = input("Digite o nome do Produto B: ")
produto_preco2 = float(input("Digite o preço do Produto B: "))
produto2 = Produto(produto_nome2, produto_preco2)

cliente_nome = input("Digite o nome do cliente: ")
cliente_endereco = input("Digite o endereço do cliente: ")
cliente = Cliente(cliente_nome, cliente_endereco)

quantidade_produto1 = int(input("Digite a quantidade do Produto A: "))
quantidade_produto2 = int(input("Digite a quantidade do Produto B: "))

pedido = Pedido(cliente)
pedido.adicionar_produto(produto1, quantidade_produto1)
pedido.adicionar_produto(produto2, quantidade_produto2)

carrinho = Carrinho()
carrinho.adicionar_pedido(pedido)

venda = Venda(carrinho)

relatorio = Relatorio()
relatorio.gerar_relatorio(venda)
