# Questão 01
# Crie um programa que permita fazer a conversão cambial entre Dólares e Reais. Considere como taxa de câmbio US$ 1,00 = R$5,27.
# Leia um valor em Dólares pelo teclado e mostre o correspondente em Reais.

# Solução do exercício

taxa_de_cambio = 5.27
valor_reais = float(input())
reais = valor_reais * taxa_de_cambio
print(f'{reais:.2f}')