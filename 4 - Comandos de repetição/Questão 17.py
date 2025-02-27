# Questão 17
# Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. 
# Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.

# Solução do exercício

investimento1 = float(input())
investimento2 = float(input())
investimento3 = float(input())
premio = float(input())

total_investido = investimento1 + investimento2 + investimento3

parte1 = (investimento1 / total_investido) * premio
parte2 = (investimento2 / total_investido) * premio
parte3 = (investimento3 / total_investido) * premio

print(f"{parte1:.2f}")
print(f"{parte2:.2f}")
print(f"{parte3:.2f}")
