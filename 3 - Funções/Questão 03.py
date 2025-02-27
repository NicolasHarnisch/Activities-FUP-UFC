# Questão 03
# Faça uma função que, a partir das medidas dos lados de um retângulo, calcule a área e o perímetro deste retângulo.

# Solução do exercício

def funcao(lado1, lado2):
    area = lado1 * lado2
    perimetro = 2 * (lado1 + lado2)
    return area, perimetro