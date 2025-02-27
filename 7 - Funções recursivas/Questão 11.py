# Questão 11
# O máximo divisor comum dos inteiros x e y é o maior inteiro que é divisível por x e y. Escreva uma função recursiva mdc que retorna o máximo divisor comum de x e y. 
# O mdc de x e y é definido como segue: se y é igual a 0, então mdc(x,y) é x; caso contrário, mdc(x,y) é mdc (y, x%y), onde % é o operador resto da divisão.

# Solução do exercício

def mdc(x1, x2):
    if x2 == 0:
        return x1
    else:
        return mdc(x2, x1 % x2)

# Pra rodar o programa
x1 = int(input(""))
x2 = int(input(""))
y = mdc(x1, x2)
print(f"{y}")