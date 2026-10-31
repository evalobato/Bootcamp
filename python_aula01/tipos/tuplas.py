#diferente das listas as tuplas não aceitam alterações

nomes = ('Ana', 'Eva', 'Maria', 'Ana') #forma de declarar uma tupla

#forma de acessar um item dentro da tupla
print('Eva' in nomes)

print(nomes[0])#printa o que está na primeira posição

print(nomes[1:2]) #pega o primeiro até o segundo, sem incluir o segundo

print(nomes[1:3])
print(nomes[1:-1])#pega o último, [-2] antepenúltimo  
print(nomes[2:]) # pega os elementos a partir do segundo


print(type(nomes))
print(nomes)