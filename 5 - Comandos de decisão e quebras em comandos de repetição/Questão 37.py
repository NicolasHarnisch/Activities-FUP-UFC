# Questão 37
# Faça uma função chamada de simplificada que receba como parâmetro o numerador e o denominador de uma fração. 
# Esta função deve simplificar a fração recebida dividindo o numerador e denominador pelo maior fator possível.
# Por exemplo, a fração 36/60 simplificada para 3/5 dividindo o numerador e denominador por 12.

# Solução do exercício

def funcao(a, b):
    while b:
        a, b = b, a % b
    return a

def simplificar(numerador, denominador):
    divisor_comum = funcao(numerador, denominador)
    return numerador // divisor_comum, denominador // divisor_comum

# Pra rodar o programa
x1 = int(input(""))
x2 = int(input(""))
y1, y2 = simplificar(x1, x2)
print(f"{y1}")
print(f"{y2}")