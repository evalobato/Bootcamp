#codigo da definição da classe, quanto do produto
#classes e objetos, a classe é um molde e os objetos vão herdar as características dessa classe
 #pass #se fosse uma classe vazia seria possivel colocar o pass
class Produto:
   def __init__(self, nome, preco = 1.99, desc = 0): essa função é usada para instanciar um novo objeto, ela que vai inicializar os dados do novo objeto, p python trabalha com o conceito que não tem nada implicito 
   #a propria referencia para instacia passada pela parâmtro (self) para um metódo que é um metodo de instacia, mais um parâmetro chamado nome, preço com valor não variável
    self.nome = nome #atribuir o nome do porduto que eu passei, para ser um atributo de dentro do onjeto, criando-o dinamicamente, que acabou de ser instanciado
    #atributo dentro do objeto
    self.preco = preco #tem que inicializar
    self.desc = desc #baseado no que foi passado na inicialização
#para instânciar um produto
p1 = Produto('Caneta') # Prouduto.__init__()passei um atributo para o meu objeto, criei um atributo dentro da instacia que foi criada com meu init
p2 = Produto('Caderno', 12.99) #passa o preco aqui

print(p1.nome, p2.nome)#utiliza o nome para acessar o atributo de uma classe, 
print(p1.preco, p2.preco)