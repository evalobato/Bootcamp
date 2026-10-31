#os atributos de instância serão um para cada instância, enquanto os de classe são compartilhados entre elas
class Contador:
    contador = 0 #definindo um atributo diretamente dentro da classe - atributo de classe

    def inst(self):
         return 'Estou bem' #neste caso sempre preciso de uma instância para chama-lo

    
    def inc_maluco(self):
         self.contador = self.contador + 1 #ele não viu contador na instacia , e pegou o valor 0 de dentro da classe, e nesse momento esta criando um atributo chamado contador dentro da instãncia que é diferente do que pertence à classe; e quando for acessar o contador da classe,e ele continuará sendo 0, são dois valores diferentes
         return self.contador

     #criar um metodo que pertence à classe e não à instãncia, usa-se decoretor

    @classmethod #método de classe 
    def inc(cls): #em vez que receber o self que é uma instância, eu recebo uma classe    
        cls.contador += 1
        return cls.contador 

    @classmethod #quando tem um metodo de classe, não é preciso criar uma instância 
    def dec(cls): #em vez que receber o self que é uma instância, eu recebo uma classe    
            cls.contador -= 1
            return cls.contador   

    @staticmethod
    def mais_um(n): #metodo estático quando não precisar acessar nada que pertença à classe, também não preisa da instacia
         return n + 1


#c1 = Contador ->cria uma instância
#mas não necessariamente preciso criar uma instãncia, ja que é um metodo pertencente à classe, posso acessar diretamente via classe/metodo  podendo fazer dessa forma:

#=> estático
print(Contador.main_um(99))

#=> de classe
# print(Contador.inc())
# print(Contador.inc())
# print(Contador.inc())
# print(Contador.dec())
# print(Contador.dec())
# print(Contador.dec())


# => com instacia
# print(c1.inc())
# print(c1.inc())
# print(c1.inc())
# print(c1.dec())
# print(c1.dec())
# print(c1.dec())

#a partir de uma instacia de uma classe é possivel acessar uma classe, ou seja, para ter uma instãncia  tem que ter a classe(ela vai semrpe existir)