# Questão 18
# Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. 
# Faça uma função que receba quanto cada apostador investiu e o valor do prêmio, e retorne quanto cada um ganharia do prêmio com base no valor investido.

# Solução do exercício

def funcao(x1, x2, x3, x4):
    total_investido = x1 + x2 + x3  
    x1 = (x1 / total_investido) * x4  
    x2 = (x2 / total_investido) * x4  
    x3 = (x3 / total_investido) * x4  
    return x1, x2, x3