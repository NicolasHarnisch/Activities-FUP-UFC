# Questão 05
# Dados três valores inteiros, A , B e C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, verificar se é um triângulo escaleno, equilátero ou isósceles, considerando os seguintes conceitos:
# ◦ O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
# ◦ Chama-se equilátero o triângulo que tem três lados iguais.
# ◦ Denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais.
# ◦ Recebe o nome de escaleno o triângulo que tem três lados diferentes.

# Solução do exercício

def triangulo():
    a = int(input())
    b = int(input())
    c = int(input())
    
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            print("Triangulo equilatero")
        elif a == b or b == c or a == c:
            print("Triangulo isosceles")
        else:
            print("Triangulo escaleno")
    else:
        print("Nao triangulo")

triangulo()
