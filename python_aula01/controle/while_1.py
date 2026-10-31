x = 10

#while x: #while com um número determinado de repetições
  #  print(x)
 #   x -= 1 #quando x for igual a 0, sai do laço

print(x)
total = 0
nota = 0.0
qtde = 0

while nota != -1: #diferente do for o while não tem uma quatidade determinada de repetições, enquanto for verdadeira fica no while, e quando for falsa sai do laço de repetição
   nota = float(input("Informe a nota ou -1 para sair: "))
   if nota != -1:
       qtde += 1
       total += nota

print(f"a média da turma é {total/qtde}")