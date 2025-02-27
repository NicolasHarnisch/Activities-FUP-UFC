# Quesão 26
# Faça uma função que receba como parâmetro o ângulo x (em radianos) e um valor inteiro positivo n . 
# Calcule o valor do seno desse ângulo usando a respectiva série de Taylor: sin(x) = x – x3/3! + x5/5! - … + (-1)n (x2n+1)/(2n+1)!.

# Solução do exercício

def funcao(x, n):
    
    termo = x
    soma = termo
    for i in range(1, n + 1):
        termo *= -x*x / ((2*i)*(2*i+1))
        soma += termo
        
    return soma

# Pra rodar o programa
x1 = float(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y:.8f}")