# Questão 27
# Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o fatorial exponencial desse número. 
# Um fatorial exponencial é um inteiro positivo n elevado à potência de n − 1 , que por sua vez é elevado à potência de n − 2 e assim por diante. Ou seja: n(n−1)^(n−2)^···^1.

# Solução do exercício

def funcao(n):
    exp = n - 1
    for j in range(1, n - 1):
        exp = exp ** j
    resultado_final = n ** exp
    return resultado_final