# Questão 32
# Faça um programa para ler uma lista de nomes dos alunos de uma turma de até 5 alunos. O programa deve solicitar ao usuário os nomes dos alunos, 
# sempre perguntando se ele deseja inserir mais um nome na lista. Uma vez lidos todos os alunos, o usuário irá indicar um nome que ele deseja verificar 
# se está presente na lista, e o programa deve procurar pelo nome (ou parte deste nome) e, se encontrar, 
# deve exibir na tela o nome completo e o índice do vetor onde está guardado este nome.

# Solução do exercício

def main():
    alunos = []
    
    while len(alunos) < 5:
        nome = input("Aluno: ")
        
        if nome.isdigit():
            break
        
        alunos.append(nome)

        if len(alunos) < 5:
            continuar = input("Deseja inserir novo aluno? [S/N] ").strip().upper()
            if continuar != 'S':
                break

    nome_pesquisa = input("Aluno para pesquisa: ")
    
    encontrados = []
    for i, aluno in enumerate(alunos):
        if nome_pesquisa in aluno:
            encontrados.append((aluno, i))

    if encontrados:
        for aluno, indice in encontrados:
            print(aluno)
            print(indice)

if __name__ == "__main__":
    main()
