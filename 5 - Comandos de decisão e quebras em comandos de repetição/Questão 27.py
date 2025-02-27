# Questão 27
# Escreva um algoritmo que leia um conjunto de n números e mostre qual foi o menor e o maior valor fornecido.

# Solução do exercício

n = int(input())
maior = float(input())  
menor = maior

for i in range(1, n):  
    numero = float(input())  
    
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"{menor:.2f}")
print(f"{maior:.2f}")
