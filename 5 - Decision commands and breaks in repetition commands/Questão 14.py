# Questão 14
# Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
# ◦ adição (opção 1)
# ◦ subtração (opção 2)
# ◦ multiplicação (opção 3)
# ◦ divisão (opção 4)
# ◦ saída (opção 5)
# O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. 
# O programa só termina quando for escolhida a opção de saída (opção 5).

# Solução do exercício

def calculadora():
    while True:
        print("1 - Adicao")
        print("2 - Subtracao")
        print("3 - Multiplicacao")
        print("4 - Divisao")
        print("5 - Saida")

        opcao = int(input())

        if opcao == 5:
            break 

        num1 = float(input())
        num2 = float(input())

        if opcao == 1:
            resultado = num1 + num2
            print(f"{resultado:.2f}")
        elif opcao == 2:
            resultado = num1 - num2
            print(f"{resultado:.2f}")
        elif opcao == 3:
            resultado = num1 * num2
            print(f"{resultado:.2f}")
        elif opcao == 4:
            if num2 == 0:
                 print("Erro")
            else:
                resultado = num1 / num2
                print(f"{resultado:.2f}")
        
calculadora()
