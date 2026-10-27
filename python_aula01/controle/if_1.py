#pegar a entrada do usuário, que neste caso será uma nota válida, para visualizar se passou de ano, reprovou ou estar de recuperação

nota = float(input("Informe a nota do aluno(a): "))

if nota >= 9: #se esta situação for verdadeira, execute o bloco de código que pertence a ele indicado pela identação
    print("Duas palavras: para bens! :D")
    print("Quadro de Honra")

elif nota >= 7: #junção de if + else, utilizada para caso não seja os casos de if e else
    print("Aprovado")
elif nota >= 5.5:
    print("Recuperação")

elif nota >= 3.5:
    print("Recuperação + Trabalho")
else: #se a situação anterior for falsa, execute o que esta neste bloco de código
    print("Reprovado")
print(nota)

