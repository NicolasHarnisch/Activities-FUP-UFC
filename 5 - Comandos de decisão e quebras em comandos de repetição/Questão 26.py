# Quesão 26
# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

# Solução do exercício

maior = None
menor = None

for i in range(10):
    numero = int(input())
    
    if maior == None:
        maior = numero
    elif numero > maior:
        maior = numero
    
    if menor == None:
        menor = numero
    elif numero < menor:
        menor = numero

print(f"{menor:.2f}")
print(f"{maior:.2f}")
