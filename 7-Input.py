"""

nome = input ("Digite seu nome: \n")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

print ("\nAluno:", nome, "\nMédia:", media)

"""

"""
nDigitado = int(input ("A tabuada de qual número você deseja ver? "))

print(nDigitado, " * 1 =", nDigitado * 1)
print(nDigitado, " * 2 =", nDigitado * 2)
print(nDigitado, " * 3 =", nDigitado * 3)
print(nDigitado, " * 4 =", nDigitado * 4)
print(nDigitado, " * 5 =", nDigitado * 5)
print(nDigitado, " * 6 =", nDigitado * 6)
print(nDigitado, " * 7 =", nDigitado * 7)
print(nDigitado, " * 8 =", nDigitado * 8)
print(nDigitado, " * 9 =", nDigitado * 9)
print(nDigitado, " * 10 =", nDigitado * 10)

"""

"""
anoatual = int(2023)
anonascimento = int(input("Digite o ano que você nasceu: "))

idade = (anoatual - anonascimento)

print ("Você tem:",idade, "anos de idade.")

"""

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

# Exemplo de Uso
produto1 = Produto("Produto A", 50.0)
produto2 = Produto("Produto B", 30.0)

cliente = Cliente("Cliente1", "Rua ABC, 123")

pedido = Pedido(cliente)
pedido.adicionar_produto(produto1, 2)
pedido.adicionar_produto(produto2, 1)

carrinho = Carrinho()
carrinho.adicionar_pedido(pedido)

venda = Venda(carrinho)

relatorio = Relatorio()
relatorio.gerar_relatorio(venda)
