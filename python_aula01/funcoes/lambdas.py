from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
] #uma lista com diciónarios dentro
#filter -> filtrar elementos dentro de uma lista
#lambda -> função anônima, sem nome
#portando é possivel criar uma função sem nome e atribuir ela a uma variável de forma que possa chama-lá depois

aluno_aprovado = lambda aluno: aluno['nota'] >= 7 #vai retornar um valor booleano
#essa expressão cria uma função anônima que recebe um aluno e verifica se sua nota é maior ou igual a 7
#aluno_honra = lambda aluno: aluno['nota'] >= 9
obter_nota = lambda aluno : aluno ['nota']

somar = lambda a,b: a + b

alunos_aprovados = filter(aluno_aprovado, alunos) #filtra os alunos que possuem nota maior ou igual a 7, tem um laço for inbutido dentro dessa função, se for verdadeira, estará presente no lista final
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados)) #tranformar o aluno que foi passado apenas para um valor do tipo float, que foi a nota desse aluno, passa a função que obtem o valor que no caso é lambda e a estrutura que vai ser usada para o retorno do filter(filter object)
#print(obter_nota(alunos[2])) possivel obter as notas dos alunos

total = reduce(somar, notas_alunos_aprovados, 0)
print(total / len(alunos_aprovados)) #media de nota dos alunos parovados

# 1. primeiro filtrou as notas a partir do filter, depois o map gerou o resultado de saída do terminal []
#2. pode-se aplicar o reduce para somar tudo