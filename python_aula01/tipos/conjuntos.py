#não aceitam elementos duplicados, e não é uma estrutura indexada (é uma coleção de dados em que cada elemento ocupa uma posição numérica específica e ordenada, chamada de índice), diferente das tuplas e listas

print({1,2,3})
print(type({1,2,3}))#class set
print({1,2,3,3,3,3})

conj= {1,2,3,3,3,3}
print(conj) #vai ser printado apenas [1,2,3]
print(len(conj))#tem 3 elementos