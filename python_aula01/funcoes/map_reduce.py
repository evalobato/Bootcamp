from functools import reduce # como não esta entre o builtins do python, é necessário importar o reduce do módulo functools

def somar_nota(delta): #não tenho a nota, mas sei quanto quero somar a ela que é o delta
    def somar (nota):
        return nota + delta
    return somar


notas = [6.4, 7.2, 5.8, 8.4]

notas_finais_1 = list(map(somar_nota(1.5), notas))#passando como parâmetro para o map uma função e o array que vai ser usado como parâmetro na função passada
notas_finais_2 = list(map(somar_nota(1.6), notas))
#com uma linha de código consegue trasnformar uma lista em outra lista passando um função que fará um mapeamento de cada uma das coisas para outra, podendo transformar varios elemntos em uma lista e qualquer coisa

#o map é mais simples resolver esse problema, uma função que pega uma lista, vai converter em outra lista do mesmo tamanho, só que foi feito um mapeamento de uma informação para a outra
print(notas_finais_1)
print(notas_finais_2)

#reduce é respomsavel por pegar uma lista percorrer por cada um dos elementos, e chamando uma fução,sendo que o primeiro parâmentro é um acumulador e o segundo é o elemento atual , assim tendo um código mais reduzido passando uma função como parâmetro para outra funçã́o


def somar(a,b):
    return a + b

#reduce é respomsavel por pegar uma lista percorrer por cada um dos elementos, e chamando uma fução,sendo que o primeiro parâmentro é um acumulador e o segundo é o elemento atual , assim tendo um código mais reduzido passando uma função como parâmetro para outra funçã́o
total = reduce(somar, notas, 0)#(função, lista, valor inicial), tenho o valor total nessa linha, apenas com essa chamada reduce, pegou todos os elementos e saiu somando
print(total)
# for i, nota in enumerate(notas):#também uma função builtins do python
#     notas[i] = nota + 1.5


# for i in range (len(notas)): #possivel também executar dessa forma, na qual irá percorrer do tamanho do array
#     notas[i] = notas[i] + 1.5


#a diferença entre eles é que o map() transforma cada item de um iterável e devolve uma nova coleção com a mesma quantidade de elementos, enquanto a função reduce() combina todos os itens em um único valor final