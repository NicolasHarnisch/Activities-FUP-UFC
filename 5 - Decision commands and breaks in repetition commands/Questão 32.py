# Questão 32
# Faça um algoritmo que, dados dois números inteiros, seja capaz de obter o quociente inteiro da divisão entre o maior e o menor deles. 
# Não use a operação de divisão (/), nem a operação de divisão inteira (//) e nem a operação de resto da divisão inteira (%).

# Solução do exercício

x = int(input())
y = int(input())

if x < y:
    x, y = y, x

quociente = 0

while x >= y:
    x -= y
    quociente += 1

print(quociente)
