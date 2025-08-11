# Questão 17
# Faça um programa que desenhe uma linha na tela usando vários símbolos de igual (Ex: ========). O programa deve ler quantos sinais de iguais serão mostrados.

# Solução do exercício

def desenha_linha(n):
    linha = "=" * n
    return linha

x = int(input())
resultado = desenha_linha(x)
print(resultado)