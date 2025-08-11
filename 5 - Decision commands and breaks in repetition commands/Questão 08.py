# Quesão 08
# Faça um programa que receba dois números e execute as operações listadas a seguir de acordo com a escolha do usuário:
# ◦ 1: Média entre os números digitados
# ◦ 2: Diferença do maior pelo menor
# ◦ 3: Produto entre os números digitados
# ◦ 4: Divisão do primeiro pelo segundo
# Se a opção digitada for inválida, mostrar uma mensagem de erro e terminar a execução do programa. Dica do Brother: Na operação 4 o segundo número deve ser diferente de 0.
# Solução do exercício

def operacoes():
    n1 = float(input())
    n2 = float(input())
    opcao = int(input())

    if opcao == 1:
        media = (n1 + n2) / 2
        print(f"{media:.2f}")
    elif opcao == 2:
        diferenca = abs(n1 - n2)
        print(f"{diferenca:.2f}")
    elif opcao == 3:
        produto = n1 * n2
        print(f"{produto:.2f}")
    elif opcao == 4:
        if n2 == 0:
            print("Erro")
        else:
            divisao = n1 / n2
            print(f"{divisao:.2f}")
    else:
        print("Erro")

operacoes()
