#PEP - proposta de melhoria do python
#empactou vários parâmentros e empacotou dentro de uma tupla ou diciónario(fem um pep)

def soma(*nums): #permitem que uma função receba um número variável de argumentos, tornando a criação de funções mais flexível -> tupla
    total = 0
    for n in nums:
        total+= n
    return total


def resultado_final(**kwargs): #keyword arguments, ou "argumentos de palavra-chave") permite que uma função em Python receba um número variável de argumentos nomeados no formato, mpacota todos esses argumentos extras em um -> dicionário comum (dict).
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'
    return f'{kwargs["nome"]} foi {status} '   


