# Questão 33
# Dado um número n inteiro e positivo, dizemos que n é perfeito se n for igual à soma de seus divisores positivos diferentes de n. 
# Construa um programa que verifica se um dado número é perfeito. Ex: 6 é perfeito, pois 1 + 2 + 3 = 6.

# Solução do exercício

n = int(input())

soma = 0

for i in range(1, n):
    if n % i == 0:
        soma += i

if soma == n:
    print("Perfeito")
else:
    print("Nao perfeito")
