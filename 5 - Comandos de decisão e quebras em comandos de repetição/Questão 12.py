# Questão 12
# Faça um programa que leia um valor digitado pelo usuário e imprima os resultados com base na tabela.
# ◦ 1: Bom Dia - Boa Tarde - Boa Noite
# ◦ 2: Por Favor :) - Com Licença :D - Muito Obrigado ;)
# ◦ 3: Por Gentileza - Você poderia - Desculpe
# ◦ 4: Boa Sorte - Tenha Fé
# ◦ Outro: Estudar vale muito a pena não é !?

# Solução do exercício

def respostas(valor):
    if valor == 1:
        print("Bom Dia - Boa Tarde - Boa Noite")
    elif valor == 2:
        print("Por Favor :) - Com Licenca :D - Muito Obrigado ;)")
    elif valor == 3:
        print("Por Gentileza - Voce poderia - Desculpe")
    elif valor == 4:
        print("Boa Sorte - Tenha Fe")
    else:
        print("Estudar vale muito a pena!")

valor = int(input())
respostas(valor)
