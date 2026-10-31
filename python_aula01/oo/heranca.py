class Carro:
    def __init__(self):
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade
    
    def acelerar(self):
        self.__velocidade += 5 #sempre que o usuário acelerar, vai acelerar de 5 em 5
        return self.__velocidade
    def frear(self):
         self.__velocidade -= 5 #decremeta de 5 em 5
         return self.__velocidade

class Uno(Carro): #a classe Uno() vai herdar os métodos de Carro(), de forma que é possível instanciar a classe e chama-lá normalmente
    pass #como não precisa ter o métodos aqui, basta utilizar o pass

class Ferrari(Carro):
    def acelerar(self): #quero sobrescrever o método acelerar que foi criado na classe Carro
            super().acelerar() #metodo super para referênciar 
            return super().acelerar() #chamando o acelerar() duas vezes, acelerando mais rápido que o original, Carro()

# outros membros dentro de uma classe, um metodo de instacia, de classe um instático
c1 = Ferrari()
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())
print(c1.frear())