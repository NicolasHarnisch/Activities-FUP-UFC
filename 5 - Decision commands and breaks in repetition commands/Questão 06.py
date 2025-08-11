# Questão 06
# Faça um programa que leia 3 notas, verifique se as notas são válidas e exiba na tela a média destas notas com duas casas decimais. 
# Uma nota válida deve ser, obrigatoriamente, um valor entre 0.00 e 10.00, onde caso a nota não possua valor válido, 
# este fato deve ser informado ao usuário e o programa termina.

# Solução do exercício

def funcao():
    soma = 0
    for i in range(3):
        x = float(input())
        if 0 <= x <= 10:
            soma += x
        else:
            print('Nota invalida')
            return
    media = soma / 3
    print(f"{media:.2f}")

funcao()
