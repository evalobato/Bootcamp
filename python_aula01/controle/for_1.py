#!python

for i in range(10): #esse laço de repetição irá executar os números de 0 a 9
    print(i, end=' ')

print('')
for i in range(1, 11): #esse laço de repetição irá executar os números de 1 a 10, por padrão inicia no zero, porem pode ser escolhido outro número para o iício
   print(i, end=' ')

print('')
for i in range(1, 100, 7): #esse laço de repetição irá executar os números de 1 a 100, pulando de 7 em 7, definindo o inicio, meio e fim
    print(i, end=' ')

print('')
for i in range(20, 0, -3): #esse laço de repetição irá executar os números de 20 a 0, decrementando 3
   print(i, end=' ')

print('')
nums = [2,4,6,8]
for n in nums: # a partir do laço é possível percorrer a lista de números
   print(n, end=' ') # para printar na tela todos os números na mesma linha, é possível usar o end, que por padrão é uma quebra de linha mas que também pode ser usado para adicionar formatação ao que será visível na tela
print('')

texto = "Python é muito massa!"

for letra in texto:
   print(letra, end = " ")
print('')

for n in {1,2,3,4,4,4,4,}: # o set também pode ser percorrido
  print(n, end = " ")

produto = {
    'nome' : 'Caneta',
    'preco' : 8.80,
    'desconto': 0.5
}
print('')

for atrib in produto: #forma de percorrer um dicionário, atributos são as chaves
    print(atrib, '==>', produto[atrib], end=' ') #vai printar os atributos e os valores a eles atribuidos
print('')

for atrib, valor in produto.items(): #outra forma de percorrer um dicionário, pegando o atributo e o valor
    print(atrib, '=>', valor, end=' ') 
    
print('')

for atrib in produto.values(): #outra forma de percorrer um dicionário, utilizando apenas os valores
    print(valor, end=' ') 
print('')

for atrib in produto.keys(): #outra forma de percorrer um dicionário, utilizando os valores e as chaves
    print(valor, end=' ') 