aluno = {
    'nome' : 'Eva Lobato',
    'nota' : 9.2,
    'ativa' : True
} #e usa um par de {}, assim como no set, mas ele funciona do tipo chave, valor, sem ser a indexação numérica, ela é feita de forma textual(string)
 


print(type(aluno))
print(aluno['nome']) #a partir da chave consegue acessar o valor
print(aluno['nota'])
print(aluno['ativa'])
print(len(aluno))