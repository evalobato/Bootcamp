#codigo da definição da classe, quanto do produto
#classes e objetos, a classe é um molde e os objetos vão herdar as características dessa classe
 #pass #se fosse uma classe vazia seria possivel colocar o pass
#como criar uma instância a partir de uma classe, como criar um contrutor a partir de valores que foram passados como padrão, foram definidos comportamentos , chamando métodos e outros com o property
class Produto:
   def __init__(self, nome, preco = 1.99, desc = 0):
    # essa função é usada para instanciar um novo objeto, ela que vai inicializar os dados do novo objeto, p python trabalha com o conceito que não tem nada implicito, cada parâmetro passado é um dado
   #a propria referencia para instacia passada pela parâmtro (self) para um metódo que é um metodo de instacia, mais um parâmetro chamado nome, preço com valor não variável
        self.nome = nome #atribuir o nome do porduto que eu passei, para ser um atributo de dentro do onjeto, criando-o dinamicamente, que acabou de ser instanciado
        #convenção para atributos privados, colocar dois (__) antes do nome do atributo
    #atributo dentro do objeto
        self.__preco = preco #tem que inicializar
        self.desc = desc #baseado no que foi passado na inicialização
   @property
   def preco(self): #uma outra forma de ter acesso ano, com o decoretor e a função, apenas para ler
       return self.__preco # pode retornar como um real, mas o ideial é com o próprio valor , para o usuario poder realizar algum calculo, ja que foi passado como privado
   
   #o ideial é criar acessores, para acessar

   @preco.setter
   def preco(self, novo_preco):#metodo setter para alterar o preço
           if novo_preco > 0:
            self.__preco = novo_preco
       
    #existe um conceito no python chamado decoretor
   @property #faz com o que vem a baixo ser entendindo como um variável e não como um metódo e quando chaar ele, chama como se fosse uma tributo
    #um metodo para calcular o preço com desconto
    #sempre que tiver um metodo que pertence a instância o primeiro parâmtro é sempre o self, como os dados ja pertencem a instância não é preciso passar o preço e o desconto novamente
   def preco_final(self):
        return (1 - self.desc) * self.__preco #dessa forma tem-se o preço final 


#para instânciar um produto
p1 = Produto('Caneta', 10, 0.1) # o python vai executar como se fosse 'Prouduto.__init__(p1,...)', passando um atributo para o objeto, cria-se um atributo dentro da instâcia que foi criada no init
p2 = Produto('Caderno', 14, 0.5) #passa o preco aqui

p1.preco = 70.88 
p2.preco = 17.89

print(p1.nome, p1.preco, p1.desc, p1.preco_final)#utiliza o nome para acessar o atributo de uma classe, chama o prelo final com parâmetros já que é um método
print(p2.nome,p2.preco, p2.desc,p2.preco_final) #criou-se outro atributo, mas o preco.final é calculado baseado em outros atributo, se chamar como função, vai dar problema 
#se fizer o atributo dessa forma '_Produto__nome' da para voltar a acessar ele quando for privado, faz como se fosse um conersaão de nomes e internamente muda o __nome para esse outro padrão
#mas se forçar para acessar dessa forma pode estar querendo violar a liguagem