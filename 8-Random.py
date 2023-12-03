#Números randomincos - Números aleatórios

import random

print(random.randrange(10, 20))

#Gerar um númerro de ponto flutuante aleatório entre 0 e 1:
print(random.random())

# Gerar um número inteiro aleatório entre dois valores (inclusive):

print(random.randint(10, 20))

#Escolher aleatoriamente um elemento de uma lista:

frutas = ["Maça", "Banana", "Cereja"]
print(random.choice(frutas)) #Escolhe uma fruta aleatoriamente da lista.

#Embaralhar aleatoriamente uma lista:
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros) # A lista 'numeros' agora está embaralhada.

#Gera um número de ponto flutuante aleatorio em um intervalo especifico.

print(random.uniform(5.5, 9.5))