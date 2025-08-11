# Questão 04
# Ler três valores e determinar o maior entre eles.

# Solução do exercício

def maior_valor():
    a = float(input())
    b = float(input())
    c = float(input())

    if a > b and a > c:
        print(f"{a:.2f}")
    elif b > c:
        print(f"{b:.2f}")
    else:
        print(f"{c:.2f}")

maior_valor()
