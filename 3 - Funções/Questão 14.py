# Questão 14
# Faça uma função que receba um número inteiro positivo de três dígitos (de 100 a 999). 
# Retorne outro número formado pelos dígitos invertidos do número lido. Exemplo: Entrada = 123, Saída = 321.

# Solução do exercício

def funcao(x):
    numero_invertido = int(str(x)[::-1])
    return numero_invertido
