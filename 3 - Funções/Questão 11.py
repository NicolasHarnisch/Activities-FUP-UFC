# Questão 11
# Crie uma função que, dados três valores, retorne a soma dos quadrados dos três valores e o quadrado da soma dos três valores.

# Solução do exercício

def funcao(x1, x2, x3):
    soma_quadrados = x1**2 + x2**2 + x3**2
    quadrado_soma = (x1 + x2 + x3)**2
    
    return soma_quadrados, quadrado_soma

