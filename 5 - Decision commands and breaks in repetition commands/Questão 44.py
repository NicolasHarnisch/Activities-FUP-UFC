# Questão 44
# Faça um programa que receba uma frase e imprima-a de maneira invertida, trocando as letras A (maiúsculas ou minúsculas) por *. 
# Não use nenhuma funcionalidade do python que já faça isso.

# Solução do exercício

def inverter(frase):
    frase_invertida = ""
    
    for i in range(len(frase) - 1, -1, -1):
        invertido = frase[i]
        if invertido == 'a':
            frase_invertida += '*'
        elif invertido == 'A':
            frase_invertida += '*'
        else:
            frase_invertida += invertido
    
    return frase_invertida

def main():
    frase = input("")
    resultado = inverter(frase)
    print(resultado)

main()
