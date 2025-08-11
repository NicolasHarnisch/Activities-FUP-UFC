# Questão 06
# Considerando o dicionário com chaves “x”, “y” e “z” para representar um vetor tridimensional, implemente uma função que calcule a soma de dois vetores, 
# e um programa que peça valores para o usuário, use essa função, e mostre o resultado.

# Solução do exercício

def calcula(v1, v2):
    return {
        'x': v1['x'] + v2['x'],
        'y': v1['y'] + v2['y'],
        'z': v1['z'] + v2['z']
    }


def main():
    valores = []
    for i in range(6):
        valor = float(input())
        valores.append(valor)

    vetor1 = {'x': valores[0], 'y': valores[1], 'z': valores[2]}
    vetor2 = {'x': valores[3], 'y': valores[4], 'z': valores[5]}

    resultado = calcula(vetor1, vetor2)

    print(resultado)


if __name__ == "__main__":
    main()
