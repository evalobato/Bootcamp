#para criar um  variável, não possui palavra reservada, tem que escrever no nome(identificador da variável), o tipo dela e o valor que ela recebe

a = 6
b = 3

print(a+b)

texto = 'Sua idade é...' #string
idade = 23  #inteiro

#print(texto + idade)
print(f'{texto}{idade}') #o python não permite concatenar string e inteiro, porém há formas de utilizar os dois tipos de variáveis, que é utilizando o formato (f’{texto} {idade}’)

print(3 * 'bom dia ') #no terminal vai aparecer três vezes 'bom dia'
saudacao = 'oi '
print(3 * saudacao )

PI = 3.14 #em python não existe constante, porém há uma convenção de que ao usar letras em capslock elas serão utilizadas como constantes


raio = float(input('informe o raio da circuferência: ')) #input coleta dados digitados pelo usuário no terminal
area = PI * pow(raio,raio) #função utilizada para calcular a potenciação de um número
print(f'a area da circ é de {area}')
