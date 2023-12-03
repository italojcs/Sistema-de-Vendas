#Imprimindo a posição das letras

posicaoLetra = "Python"
print(posicaoLetra[0])
print(posicaoLetra[1])
print(posicaoLetra[2])
print(posicaoLetra[3])
print(posicaoLetra[4])
print(posicaoLetra[5])

frase = "Olá, mundo!"
parte = frase[4:8]
print(parte) #Saida: mun

primeiros = frase[:5]
print(primeiros) #Olá, 

ultimos = frase[-6:]
print(ultimos) #mundo!


######################

frase = "O módulo de python é muito legal"
print("python" in frase)

#O operador in é usado em python para verificar a presença de um valor dentro de uma sequência, (String, lista ou tupla).

#Verifica se a palavra python está na frase.

frase2 = "O módulo de python é muito legal"
if "python" in frase2:
    print("Sim, a palavra python está presente na frase.")
if "python" not in frase2:
    print("Não, a palavra python não está presente na frase.")

##############################

#Usamos para remover espaços em branco do inicio e do final da frase.

frase3 = "              O modulo python é muito legal        "
print(frase3.strip())

##############################


#spit, join e strip são metodos muito uteis da str

frase4 = "Olá, como vai você?" 
palavras = frase4.split() #Dividindo a frase em palavras usando o espaço em branco como separador.

print(palavras)

#################################

#O metodo join() junta os elementos de uma lista em uma única string, utilizando um separador especifico entre cada elemento.

palavras2 = "['Olá,', 'como', 'vai', 'você?']"
frase5 = ' '.join(palavras) #Dividindo a frase em palavras usando o espaço em branco como separador.

print(frase5)

#################################


#Removendo espaços em branco do inicio e do final, ou um determinado caracter.

texto = "*******Olá!*********"
texto_strip = texto.strip('*')
print (texto_strip)