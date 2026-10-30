#codigo da definição da classe, quanto do produto
#classes e objetos, a classe é um molde e os objetos vão herdar as características dessa classe
 #pass #se fosse uma classe vazia seria possivel colocar o pass
class Produto:
   def __init__(self, nome): essa função é usada para instanciar um novo objeto, ela que vai inicializar os dados do novo objeto, p python trabalha com o conceito que não tem nada implicito 
   #a propria referencia para instacia passada pela parâmtro (self) para um metódo que é um metodo de instacia, mais um parâmetro chamado nome
    self.nome = nome #atribuir o nome do porduto que eu passei, para ser um atributo de dentro do onjeto, criando-o dinamicamente, que acabou de ser instanciado

#para instânciar um produto
p1 = Produto()
p2 = Produto()

print(p1, p2)