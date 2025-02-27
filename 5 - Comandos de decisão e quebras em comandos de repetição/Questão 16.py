# Questão 16
# Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido.

# Solução do exercício

def encontrar_maior_menor():
    maior = None
    menor = None
    contador = 0

    while True:
        numero = int(input())
        
        if numero < 0:
            if contador > 1:
                print(maior)
                print(menor)
            elif contador == 1:
                print(maior)
                print(maior)
            break
        
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
        
        contador += 1

encontrar_maior_menor()
