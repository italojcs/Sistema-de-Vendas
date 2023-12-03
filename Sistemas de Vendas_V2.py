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

# Função para perguntar se o usuário deseja adicionar outro produto
def adicionar_outro_produto():
    resposta = input("Deseja adicionar outro produto ao pedido? (S/N): ")
    return resposta.lower() == 's'

# Exemplo de Uso com Inputs do Usuário
carrinho = Carrinho()

while True:
    produto_nome = input("Digite o nome do Produto: ")
    produto_preco = float(input("Digite o preço do Produto: "))
    produto = Produto(produto_nome, produto_preco)

    cliente_nome = input("Digite o nome do cliente: ")
    cliente_endereco = input("Digite o endereço do cliente: ")
    cliente = Cliente(cliente_nome, cliente_endereco)

    quantidade_produto = int(input("Digite a quantidade do Produto: "))

    pedido = Pedido(cliente)
    pedido.adicionar_produto(produto, quantidade_produto)

    carrinho.adicionar_pedido(pedido)

    if not adicionar_outro_produto():
        break

venda = Venda(carrinho)

relatorio = Relatorio()
relatorio.gerar_relatorio(venda)