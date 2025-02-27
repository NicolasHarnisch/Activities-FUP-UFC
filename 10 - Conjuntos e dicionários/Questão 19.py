# Questão 19
# Defina os dicionários cujas representações gráficas são dadas na figura a seguir:
# ◦ Permita ao usuário entrar com dados para preencher 5 cadastros.
# ◦ Encontre a pessoa com maior idade entre os cadastrados
# ◦ Encontre as pessoas do sexo masculino
# ◦ Encontre as pessoas com salário maior que 1000.
# ◦ Imprima os dados da pessoa cuja identidade seja igual a um valor fornecido pelo usuário

#                                                   Cadastro  
#
#                                                    +--------------+--------------+--------------+  
#                                                    |    NOME      |  ENDEREÇO    |   SALÁRIO    |  
#                                                    +--------------+--------------+--------------+  
#                                                    | IDENTIDADE   |     CPF      | ESTADO CIVIL |  
#                                                    +--------------+--------------+--------------+  
#                                                    |  TELEFONE    |    IDADE     |     SEXO     |  
#                                                    +--------------+--------------+--------------+  
#
#                                                    O ENDEREÇO é composto de:  
#
#                                                    +--------------+--------------+--------------+  
#                                                    |     RUA      |   BAIRRO     |   CIDADE     |  
#                                                    +--------------+--------------+--------------+  
#                                                    |   ESTADO     |     CEP      |  
#                                                    +--------------+--------------+  


# Solução do exercício

produtos = []
codigos = []
for i in range(5):
    produto = {}
    produto['codigo'] = int(input())
    produto['nome'] = input()
    produto['preco'] = float(input())
    produto['quantidade'] = int(input())
    codigos.append(produto['codigo'])
    produtos.append(produto)

while True:
    for i in range(5):
        print(produtos[i])
    cod = int(input())
    if cod == 0:
        break
    qtd = int(input())
    if not cod in codigos:
        print('Impossivel atender ao pedido, codigo nao encontrado')
    for prod in produtos:
        if prod['codigo'] == cod:
            if qtd <= prod['quantidade']:
                prod['quantidade'] = prod['quantidade'] - qtd
            else:
                print('Impossivel atender ao pedido, produto sem estoque suficiente')
