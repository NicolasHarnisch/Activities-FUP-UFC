# Questão 10
# Construa um programa que leia duas strings fornecidas pelo usuário e verifique se a segunda 
# string lida está contida no final da primeira, retornando o resultado da verificação.

# Solução do exercício

s1 = input("")
s2 = input("")

resultado = s2 in s1[-len(s2):]

print(resultado)