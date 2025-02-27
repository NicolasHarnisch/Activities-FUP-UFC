# Questão 15
# Faça uma função que receba um número inteiro de 4 dígitos (de 1000 a 9999) e retorne os 4 dígitos separados, cada um em uma variável diferente.

# Solução do exercício

def funcao(x):
    num_str = str(x)
    
    digito1 = int(num_str[0])
    digito2 = int(num_str[1])
    digito3 = int(num_str[2])
    digito4 = int(num_str[3])
    
    return digito1, digito2, digito3, digito4