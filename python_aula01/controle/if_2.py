a = "valor"

print(not not "valor")
a = 0 #vai avalizar para falso
a = -0.00001 #qualquer numero diferente de zero é falso
a = '' #string vazia vai ser falto
a = ' ' #string com espaço em branco vai ser verdadeira
a = [] #uma lista vazia vai ser falsa
a= {} #um conjunto vazio também é falso

if a: #se essa variavel existir, o resultado é verdadeiro
    print("Existe!!!") #vai executar esse bloco que pode ter uma ou mais sentenças
else:
    print("Não existe ou zero ou vazio...") #caso contrário executa o bloco associado ao else