print('---------------------')
print('-----CALCULADORA-----')
print('---------------------')
#nesta calculadora simples foram utilizados principios básicos de propramação orientada a objeto, como classes e métodos
class Calculadora:
    def __init__(self, a,b): #método construtor da classe, é executado para guardar os dois números dentro do objeto(self)
        self.a = a #guarda o primeiro número como argumento
        self.b = b #guarda o segundo número como argumento

    @property #o decorador transforma esse método em um atributo
    def soma(self):
        return self.a + self.b #retorna soma
    
    @property
    def subtracao(self): #retorna subtração
            return self.a - self.b

    def multiplicacao(self): #retorna multiplicação
            return self.a * self.b

    def divisao(self):
            if self.b == 0: #estrutura condicional que verifica se o b é igual a 0, para evitar o erro de divisão por 0
                return 'Digite um número diferente de 0 para b' #se for zero retorna ao usuário uma mensagem para digitar um número diferente de 0
            else:
                return self.a / self.b

    def modulo(self):
            if self.b == 0:
                return 'Digite um número diferente de 0 para b'
            else:
                return self.a / self.b
    def exponenciacao(self):
          return pow(self.a, self.b)

#instancia a classe, cria o objeto 'calculo' e passa os valores de 'a' e 'b'
calculo = Calculadora(4, 0)

#exibe os resultados
print(f'Soma: {calculo.soma}') #como foi usado o property, permite acessar o resultado passando objeto.metodo sem os parênteses
print(f'Subtração: {calculo.subtracao}')
print(f'Multiplicação: {calculo.multiplicacao()}')#como é um método normal precisa do parênteses ma chamada
print(f'Divisão: {calculo.divisao()}')
print(f'Módulo: {calculo.modulo()}')
print(f'Exponenciação: {calculo.exponenciacao()}')

