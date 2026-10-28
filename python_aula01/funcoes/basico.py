#definindo uma função, com a palavra reservada 'def', e os parametros de entrada da função, faz o procvessamento e gera uma sáida
#sempre a alguma função tem um bloco associado, e quando não tiver nada, se usa o      'pass', para avisar que é uma função vazia
#na função define um bloco e dentro desse bloco, vai exitir todo o algoritmo relacionado a essa função
#o parâmetro na função é passado dentro do parênteses,podem ser separados por ',';
#pode ter um valor padrão para determinado parâmetro, fazendo co que consiga chamar a função de duas formas diferentes, uma passando parâmetro e outra sem passar,  e não é obrigado a ter parâmetros
#a variável dentro da função só esta definida dentro da função, portanto enquando ela estiver sendo executada, ela existe
#mais fléxivel retornar alguma coisa a partir de uma chamada de função, do que amarrar o que foi feito dentro dela apenas imprimindo
def suadacao(nome = 'Pessoa', idade = 20):
    print(f'Bom dia, {nome}! \n você nem parece ter {idade} anos!') #\n para quebra de linha

#def suadacao(): #sobrescreve a nova função, porém não há uma sobrecarga no python, tendo duas funções sendo uma delas com parâmetros opcionais que faz co que consiga chamar aquela função de várias formas diferentes
    #print(f'Boa tarde!')



def soma_e_multipli(a,b,x): #agora vou querer retornar o resultado dessa operação
    return (a + b) * x #return utilizado para retornar algo pela função, passei três parâmetros e vou receber um retorno como resposta
                        #operador binário que vai aperar no b e no x
                        #muito melhor retornar algo dentro da função, do que printar dentro dela, pois não é possível fazer mais nada com o que aquela função está produzindo


if __name__ == '__main__': #para ser executado apenas quando o main for o principal, se for o arquivo inicial da aplicação, módulo principal
    suadacao('Ana', idade = 30)
#é possível acessar o nome do modulo quando acessa a variável __name__, quando chamado a partir do arquivo basico.py ele é o módulo main, pois foi a partir desse arquivo que a aplicação foi executada, chamando o interpretador do python, e se for chamado a partir do main.py, ele vai mostrar que o  nome é funcoes.basico

