# Questão 18
# Faça um programa que gerencie o estoque de um mercado e:
# ◦ Crie e leia um vetor de 5 produtos, com os dados: código (inteiro), nome (máximo 15 letras), preço e quantidade.
# ◦ Leia um pedido, composto por um código de produto e a quantidade. Localize este código no vetor e, se houver quantidade suficiente para atender ao pedido integralmente, atualize o estoque e informe o usuário. Repita este processo até ler um código igual a zero. Se, por algum motivo não for possível atender ao pedido, mostre uma mensagem informando que é “Impossivel atender ao pedido, produto sem estoque suficiente” ou “Impossivel atender ao pedido, codigo nao encontrado”.
# ◦ A cada passo, antes de ler o código, imprima o estoque do mercado.

# Solução do exercício

eletrodomesticos = []

for i in range(5):
    eletrodomestico = {}
    eletrodomestico['nome'] = input()
    eletrodomestico['potencia'] = float(input())
    eletrodomestico['tempo ativo por dia'] = float(input())
    eletrodomesticos.append(eletrodomestico)
tempo = int(input())
soma = 0

for eletro in eletrodomesticos:
    unico = eletro['potencia'] * eletro['tempo ativo por dia'] * tempo
    eletro['consumo'] = unico
    soma += unico
    
print(f'{soma:.2f}')    

for eletro in eletrodomesticos:
    nome = eletro['nome']
    consumo = eletro['consumo']
    consumo_relativo = (consumo/soma) *100
    print(f'{nome}: {consumo_relativo:.2f}')