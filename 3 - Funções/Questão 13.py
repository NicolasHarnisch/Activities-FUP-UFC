# Questão 13
# Faça uma função que receba um valor em R$ que será dividido entre três ganhadores de um concurso. Sendo que da quantia total:
# ◦ O primeiro ganhador receberá 46%;
# ◦ O segundo ganhador receberá 32%;
# ◦ O terceiro receberá o restante;
# Calcule e retorne a quantia ganha por cada um dos ganhadores.

# Solução do exercício

def funcao(x):
    ganhador1 = x * 46 / 100
    ganhador2 = x * 32 / 100
    ganhador3 = x - ganhador1 - ganhador2
    
    return ganhador1, ganhador2, ganhador3