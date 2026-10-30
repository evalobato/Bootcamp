def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

somar = soma #armazenar uma função dentro de uma variável
print(somar(3,4)) #sendo possível chamar a função a partir dessa variável

def operacao_aritmetica(fn, op1,op2): #essa função recebe como parâmetro uma outra função e dois operandos para usar na função chamada como parâmetro
    return fn(op1, op2) #chamada de função dentro da outra função

resultado = operacao_aritmetica(soma, 13, 48) #vai pegar os dois valores, a função e vai passar os operadores para ela, e o resultado vai ser retornado pro som()
print(resultado)

resultado = operacao_aritmetica(sub, 13, 48) 
print(resultado)

#essas funcionalidades ajudam o código a ser mais eficiente, e faceis de serem executados

def soma_parcial(a): #dentro dessa função foi definida outra função, 
    #processamento pesado 1 - 10s
    #processamento pesado 2 - 10s
    #processamento pesado 3 - 40s

    def concluir_soma(b):
        return a + b
    return concluir_soma #aqui retorna a função, o resultado não vai ser a soma de a = b, mas sim o resultado de uam função

#r1 =  soma_total(1,2) => 1m10s
#r2 =  soma_total(1,3) => 1m10s
#r3 = soma_total(1,4) => 1m10s
#dessa forma leva mais de 3m para fazer o processamento, passa o mesmo valor de a 3 vezes o que torna mais demorado, mesmo que as funções seguntes tenham o  mesmo valor para a 

soma_1 = soma_parcial(1) #1m
r1 = soma_1(2)
r2 = soma_1(3)
r3 = soma_1(4)
#equando aqui demorou 1m30s para todo o processamento, fezendo de forma parcial, aqui a programação fica mias funcional quando a a só é processado uma ves, levando em conta que nas três operações o a tem o mesmo valor


#fn = soma_parcial(10)
#resultado_final = fn(12) # permite que uma função interna continue acessando uma variável da função externa, mesmo depois que a função externa termina

resultado_final = soma_parcial(10)(12) # dessa coloca todos os resultados em uma única linha, para tornar a execução tardia, juntado as duas váriaveis
print(resultado_final, r1,r2,r3)