# Questão 12

# Faça um programa que receba um valor em R$ que será dividido entre três ganhadores de um concurso. Sendo que da quantia total:
# ◦ O primeiro ganhador receberá 46%;
# ◦ O segundo ganhador receberá 32%;
# ◦ O terceiro receberá o restante;
# Calcule e imprima a quantia ganha por cada um dos ganhadores.

# Solução do exercício

valor_total = float(input())

primeiro_ganhador = valor_total * 0.46
segundo_ganhador = valor_total * 0.32
terceiro_ganhador = valor_total - (primeiro_ganhador + segundo_ganhador)

print(f"{primeiro_ganhador:.2f}")
print(f"{segundo_ganhador:.2f}")
print(f"{terceiro_ganhador:.2f}")