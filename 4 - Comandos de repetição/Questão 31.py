# Questão 31
# Implemente um programa que leia duas strings, str1 e str2, e um valor inteiro positivo N. Concatene N vezes a string str2 ao final da string str1.

# Solução do exercício

str1 = input()
str2 = input()
n = int(input())

for i in range(n):
    str1 += str2

print(str1)
