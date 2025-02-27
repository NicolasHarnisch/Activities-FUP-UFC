# Questão 17
# questãoFaça um programa que controla o consumo de energia dos eletrodomésticos de uma casa e:
# ◦ Crie e leia 5 eletrodomésticos que contêm nome (máximo 15 letras), potência (real, em kW) e tempo ativo por dia (real, em horas).
# ◦ Leia um tempo t (em dias), calcule e mostre o consumo total (em kWh) na casa e o consumo relativo de cada eletrodoméstico (consumo/consumo total) nesse período de tempo. Apresente este último dado em porcentagem.

# Solução do exercício

devices = {}

for _ in range(5):
    nome = input().strip()
    potencia = float(input().strip())
    tempo_ativo = float(input().strip())
    devices[nome] = {
        'potencia': potencia,
        'tempo_ativo': tempo_ativo
    }

tempo_dias = int(input().strip())
consumo_total = 0

for nome in devices:
    consumo = devices[nome]['potencia'] * devices[nome]['tempo_ativo'] * tempo_dias
    devices[nome]['consumo'] = consumo
    consumo_total += consumo

# Exibe o consumo total
print(f"{consumo_total:.2f}")

# Exibe o consumo percentual de cada dispositivo
for nome in devices:
    perc = (devices[nome]['consumo'] / consumo_total) * 100
    print(f"{nome}: {perc:.2f}")
