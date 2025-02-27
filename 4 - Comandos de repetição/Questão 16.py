# Questão 16
# Faça um programa que calcule e escreva o valor de S = 1/1 + 3/2 + 5/3 + 7/4 + … + 99/50.

# Solução do exercício

s = 0
numerador = 1
for denominador in range(1, 51):
    s += numerador / denominador
    numerador += 2
print(f"{s:.10f}")