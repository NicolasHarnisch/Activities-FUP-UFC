# Questão 07
# Leia o salário de um trabalhador e o valor da prestação de um empréstimo. 
# Se a prestação for maior que 20% do salário então imprima: "Emprestimo nao concedido", caso contrário imprima: "Emprestimo concedido".

# Solução do exercício

def verificar_emprestimo():
    salario = float(input())
    prestacao = float(input())
    if prestacao > 0.2 * salario:
        print("Emprestimo nao concedido")
    else:
        print("Emprestimo concedido")

verificar_emprestimo()
