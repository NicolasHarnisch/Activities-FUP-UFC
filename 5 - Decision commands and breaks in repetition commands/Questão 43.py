# Questão 43
# Escreva um programa que leia a idade e o primeiro nome de várias pessoas. Seu programa deve terminar quando uma idade negativa for digitada. 
# Ao terminar, seu programa deve escrever o nome e a idade das pessoas mais jovens e mais velhas.

# Solução do exercício

def main():
    mais_jovem_nome = ""
    mais_jovem_idade = float("inf")
    mais_velho_nome = ""
    mais_velho_idade = float("-inf")
    
    while True:
        nome = input("")
        idade = int(input(""))
        
        if idade < 0:
            break
        
        if idade < mais_jovem_idade:
            mais_jovem_idade = idade
            mais_jovem_nome = nome
        
        if idade > mais_velho_idade:
            mais_velho_idade = idade
            mais_velho_nome = nome
    
    if mais_jovem_nome != "":
        print(f"{mais_jovem_nome}")
        print(f"{mais_jovem_idade}")
    
    if mais_velho_nome != "":
        print(f"{mais_velho_nome}")
        print(f"{mais_velho_idade}")

main()
