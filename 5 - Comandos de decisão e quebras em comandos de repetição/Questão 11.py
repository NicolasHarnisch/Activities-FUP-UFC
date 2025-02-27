# Questão 11
# Faça um programa que simule uma calculadora com as 4 operações básicas. 
# O usuário digita o primeiro número, escolhe a operação e em seguida digita o segundo número, exatamente nessa ordem. O programa deve mostrar o resultado da operação.

# Solução do exercício

def calculadora():
    num1 = float(input())
    operacao = input()
    num2 = float(input())
    
    if operacao == "+":
        print(f"{num1 + num2:.2f}")
    elif operacao == "-":
        print(f"{num1 - num2:.2f}")
    elif operacao == "*":
        print(f"{num1 * num2:.2f}")
    elif operacao == "/":
        if num2 != 0:
            print(f"{num1 / num2:.2f}")
calculadora()
