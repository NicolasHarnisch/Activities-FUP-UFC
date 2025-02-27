# Questão 02
# Faça um programa que, a partir das medidas dos lados de um retângulo, lidos via teclado, calcule a área e o perímetro deste retângulo.

# Solução do exercício

Base = float(input())
Altura = float(input())
Area = Base * Altura
print ((f'{Area:.2f}'))
Perimetro = 2 * Base + 2 * Altura
print ((f'{Perimetro:.2f}'))