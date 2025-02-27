# Questão 01
# Implemente um programa que leia o nome, a idade e o endereço de uma pessoa e armazene os dados em um dicionário. Imprima o dicionário.

# Solução do exercício

def coletar_dados():
    nome = input()
    while True:
        idade = input()
        if idade.isdigit():
            idade = int(idade)
            break
    endereco = input()
    return {"nome": nome, "idade": idade, "endereco": endereco}

if __name__ == "__main__":
    pessoa = coletar_dados()
    print(pessoa)
