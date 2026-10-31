from functools import reduce

trabalhadores = [ 
    {'nome': 'Eva', 'salario': 2500},
    {'nome': 'Roberto', 'salario': 5000},
    {'nome': 'Safira', 'salario': 3000},
    {'nome': 'Silmara', 'salario': 10000},
]

print("Os trabalhadores irão ter um aumento de 10% em seus seus salãrios ")


aumento = lambda trabalhadores: {
    'nome':trabalhadores['nome'],
    'salario': trabalhadores['salario'] * 0.1 + trabalhadores['salario']
}
aumento_sal = list(map(aumento, trabalhadores))
print(aumento_sal)

print('Soma dos salarios dos trabalhadores:')

def soma(soma_salario, aumento_sal):
    soma_salario += aumento_sal['salario'] 
    return soma_salario

resultado = reduce(soma, aumento_sal, 0)
print(resultado)
