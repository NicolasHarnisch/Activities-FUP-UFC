# Quesão 08
# Faça um programa em que troque todas as ocorrências de uma letra L1 pela letra L2 em uma string. 
# A string e as letras L1 e L2 devem ser fornecidas pelo usuário.

# Solução do exercício

texto = input("")
letra1 = input("")
letra2 = input("")

texto_modificado = texto.replace(letra1, letra2)

print(texto_modificado)
