# Questão 13
# Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). 
# Gere outro número formado pelos dígitos invertidos do número lido. Exemplo: Número Lido = 123, Número Gerado = 321.

# Solução do exercício

numero = int(input())

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

numero_invertido = (unidade * 100) + (dezena * 10) + centena

print(numero_invertido)
