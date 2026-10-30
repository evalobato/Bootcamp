#!python3

# print('Ola mundo, seja bem vindo')

# import pratica01.pacote.sub.arq
#from tipos import variaveis, basicos
#import tipos.lista
#import tipos.tuplas
#import tipos.conjuntos
#import tipos.dicionario

#import operadores.unarios
#import operadores.relacionais
#import operadores.atribuicao
#import operadores.logicos
#import operadores.ternario

#import controle.if_1
#import controle.if_2
#import controle.for_1
#import controle.while_1
#import controle.outros_exemplos

#from funcoes import basico #ou from funcoes.basico import saudacao e saudacao(), dessa forma precisa ter cuidado para caso esteja importanto funções com o mesmo nome, irá gerar conflito, e erros na aplicação
#para acessar a função é necessário acessar o name_space para importar esse módulo, quando você cria um módulo há um nome associado a ele, tanto que posso criar uma função com o mesmo nome em outro arquivo que não terá conflito
#basico.suadacao()
#basico.suadacao('Maria')
#como há um valor determinado para o parâmetro, quando ele não é passado na chamada, utiliza-se o que esta na função como padrão
#basico.suadacao('João', 33)# para acessar aquela função, é necessário passar o parâmentro posicional
#basico.suadacao(idade = 89) #pode-se passar apenas a idade
#o python não possui sobrecarga de função
#pode chamar a função de 4 formas diferentes
#a = basico.soma_e_multipli(x = 10, a = 2, b = 3) #não printa nada, pois esta apenas retornando
#b = basico.soma_e_multipli(x = 10, a = 2, b = 3)
#resultado = a + b
#print(resultado)

#from funcoes import args
#s = args.soma(1, 2, 3, 7,8,9, 10) #uma tupla
#print(s)
#resultado = args.resultado_final( nome = 'Pedro', nota = 6.3)
#print(resultado)

#from funcoes import funcional
#import funcoes.map_reduce #não esta entre o builtins do python
import funcoes.lambdas