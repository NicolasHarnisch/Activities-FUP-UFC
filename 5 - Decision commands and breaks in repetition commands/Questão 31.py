# Questão 31
# Faça um programa que receba dois números. Calcule e mostre:
# ◦ A soma dos números pares desse intervalo de números (intervalo incluindo os números dados);
# ◦ A multiplicação dos números ímpares desse intervalo (intervalo incluindo os números dados)

# Solução do exercício

def main():
    numero1 = int(input(""))
    numero2 = int(input(""))
    
    if numero1 > numero2:
        inicio = numero2
        fim = numero1
    else:
        inicio = numero1
        fim = numero2
    
    soma_par = 0
    multiplicacao_impar = 1
    impar = False  
    
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            soma_par += i  
        else:
            multiplicacao_impar *= i  
            impar = True  
    
    print(f"{soma_par}")

    if impar:
        print(f"{multiplicacao_impar}")
    else:
        print(1)

main()
