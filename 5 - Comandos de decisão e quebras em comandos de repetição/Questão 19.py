# Questão 19
# Faça um função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo, −1 se negativo e 0 se for igual a zero.

# Solução do exercício

def funcao(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0
    
# Pra rodar o Programa
x = float(input(""))
y = funcao(x)
print(f"{y}")