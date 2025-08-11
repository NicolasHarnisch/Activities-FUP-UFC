# Questão 29
# Faça um programa que receba um valor inteiro n ≥ 0 e imprima se esse número é primo ou não.

# Solução do exercício

n = int(input())

if n < 2:
    print("Nao primo")
else:
    primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break
    if primo:
        print("Primo")
    else:
        print("Nao primo")
  