pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'inteligente']

for p in pessoas: # pode-se usar um laço dentro do outra para que alterne o conteúdo descrito em cada uma das listas
    for a in adjs:
        print(f"{p} é {a}!")

for i in [1,2,3]: #não pode definir um laço vazio dessa forma
    pass #mas isso pode ser feito com a utilização do pass, conceito que será utilizado também  em classes(que gera um herança e cria uma classe vazia), não funciona sem ele

for i in range(1, 11):
    if i % 2 == 1: #retorna sempre 0 se for par, e 1 se for ímpar
        continue #sempre que valor for impar ele chama o continue, interrompe a repetição e vai pra próxima
    print(i, end=' ') #caso contrario imprime o valor de i

for i in range(1, 11):
    if i == 5:
        break #interrompe a repetição e sai do laço
    print(i, end=' ') 

print("Fim!")
