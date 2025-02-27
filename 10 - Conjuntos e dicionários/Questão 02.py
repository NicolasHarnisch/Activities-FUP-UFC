# Questão 02
# Faça um programa que preencha as informações dos modelos de cinco carros (exemplos de modelos: Fusca, Gol, Vectra, etc.) 
# juntamente com o consumo desses carros, isto é, quantos quilômetros cada um deles faz com um litro de combustível. Calcule e mostre:
# ◦ O modelo de carro mais econômico;
# ◦ Quantos quilômetros cada um dos carros cadastrados percorre com 50 litros de combustível;
# ◦ Quantos litros de combustível cada um dos carros cadastrados consomem para percorrer uma distância de 1.000 quilômetros.
# Solução do exercício

carros = {}

for i in range(5):
    modelo = input('')
    consumo = float(input())
    carros[modelo] = consumo

economico = [0, 0]
for modelo, consumo in carros.items():
    if consumo > economico[1]:
        economico = [modelo, consumo]
print(f'Carro mais economico: {economico[0]}')

for modelo, consumo in carros.items():
    print(f'Carro {modelo} percorre {consumo*50:.2f} kms com 50 litros')
for modelo, consumo in carros.items():
    print(f'Carro {modelo} precisa de {1000/consumo:.2f} litros para percorrer 1000 kms')