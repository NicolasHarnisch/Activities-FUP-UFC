# Questão 14
# Faça um programa que leia um vetor com os dados de 5 carros: marca, ano e preço. Leia um valor p e mostre as informações de todos os carros com preço menor que p. 
# Repita este processo até que seja lido um valor p = 0.

# Solução do exercício

carros = []

for _ in range(5):
    modelo = input()
    ano = int(input())
    preco = float(input())
    carros.append({'modelo': modelo, 'ano': ano, 'preco': preco})

while True:
    p = float(input())
    if p == 0:
        break
    
    carros_filtrados = [carro for carro in carros if carro['preco'] < p]
    for carro in carros_filtrados:
        print(carro)
