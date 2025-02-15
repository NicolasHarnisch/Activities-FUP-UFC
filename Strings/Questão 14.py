# Questão 14
# Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.

# Solução do exercício

numero = int(input())

milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print(milhar)
print(centena)
print(dezena)
print(unidade)
