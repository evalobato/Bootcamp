from functools import reduce
#como usar a sintaxe do list comprehension para gerar os alunos aprovados
alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
] 


somar = lambda a,b: a + b

alunos_aprovados = [aluno for aluno in alunos if aluno ['nota'] >= 7] #vai gerar uma lista com as notas dos alunos, posso utilizar o if para filtar os alunos com nota maior ou igual a 7, sem usar a função filter
notas_alunos_aprovados = [aluno ['nota'] for aluno in alunos_aprovados] 
print(notas_alunos_aprovados)
total = reduce(somar, notas_alunos_aprovados, 0)
print(total / len(alunos_aprovados))

#usou o list comprehension para filtrar os alunos que passaram em detrminado critério