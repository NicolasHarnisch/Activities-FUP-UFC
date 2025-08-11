# Questão 20
# Faça um programa que leia um vetor de 100 posições para números reais e, depois, um código inteiro. Se o código for 0, finalize o programa; 
# se o código for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem inversa. 
# Caso, o código seja diferente de 1 e 2 escreva uma mensagem informando que o código é inválido. 
# O programa sempre deve pedir outro código, e terminar somente quando o código for 0.

# Solução do exercício

vetor = []
for i in range(100):
    vetor.append(float(input()))

while True:
    codigo = int(input())
    if codigo == 0:
        break
    elif codigo == 1:
        for num in vetor:
            print(num)
    elif codigo == 2:
        for num in vetor[::-1]:
            print(num)
    else:
        print("Codigo invalido")
