# Questão 45
# O código de César é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de substituição na qual cada letra do texto é substituída por outra,
#  que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, ‘A’ seria substituído por ‘D’, ‘B’ se tornaria ‘E’, 
# e assim por diante. Implemente uma função que faça uso desse Código de César, entre com uma string e a quantidade de posições e retorne a string codificada. 
# Exemplo:
# String: A LIGEIRA RAPOSA MARROM SALTOU SOBRE O CACHORRO CANSADO
# Nova string com 3 posições: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
# Observação: caso a letra codificada passe da letra Z, ela deve voltar para o início do alfabeto.

# Solução do exercício

def funcao(texto, deslocamento):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texto_codificado = ""
    
    for letra in texto:
        if letra == " ":  
            texto_codificado += " "
            continue
        
        letra = letra.upper()
        
        if letra in alfabeto:  
            indice_inicial = alfabeto.index(letra)  
            novo_indice = (indice_inicial + deslocamento) % 26  
            texto_codificado += alfabeto[novo_indice]  
        else:
            texto_codificado += letra  
    return texto_codificado

# Pra rodar o programa
x1 = input("")
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y}")