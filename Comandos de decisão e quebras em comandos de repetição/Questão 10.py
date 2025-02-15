# Questão 10
# Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores e o quadrado da soma dos três valores.

# Solução do exercício

a = float(input())
b = float(input())
c = float(input())

soma_dos_quadrados = a**2 + b**2 + c**2
quadrado_da_soma = (a + b + c)**2

print(f"{soma_dos_quadrados:.2f}")
print(f"{quadrado_da_soma:.2f}")
