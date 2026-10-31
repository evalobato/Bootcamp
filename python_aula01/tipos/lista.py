nums = [1,2,3] #forma utilizada para declarar uma lista
print(type(nums))

nums.append(3) #append: adiciona itens à lista

nums.append(4)
nums.append(5)
print(len(nums)) #retorna retorna o número de itens (o tamanho ou a quantidade de elementos) 

nums[3] = 100 # é possivel acessar e alterar os elementos após a criação da lista, só alterando lista[indice] : x

nums.insert(0, -200) # é utilizado para adicionar um elemento em uma posição específica de uma lista existente
print(nums[-1]) #forma de ter acesso ao último intem da lista
print(nums)