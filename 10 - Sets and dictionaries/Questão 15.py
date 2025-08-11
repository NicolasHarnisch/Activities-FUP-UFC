# Questão 15
# Faça um programa que leia um vetor com dados de 5 livros: título, autor e ano. Procure um livro por título, perguntando ao usuário qual título deseja buscar. 
# Mostre os dados de todos os livros encontrados. O título procurado não precisa ser exato, ou seja, os livros encontrados devem ser aqueles que contêm o título buscado.

# Solução do exercício

livros = []

for _ in range(5):
    titulo = input().strip()
    autor = input().strip()
    ano = int(input().strip())
    livros.append({'titulo': titulo, 'autor': autor, 'ano': ano})

busca = input().strip().lower()

for livro in livros:
    if busca in livro['titulo'].lower():
        print(livro)
