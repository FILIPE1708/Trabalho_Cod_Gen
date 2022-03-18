from ag import AlgoritmoGenetico

dados = [
    {'item': 'item 1', 'peso': 4, 'valor': 6},
    {'item': 'item 2', 'peso': 3, 'valor': 5},
    {'item': 'item 3', 'peso': 2, 'valor': 2},
    {'item': 'item 4', 'peso': 8, 'valor': 10},
    {'item': 'item 5', 'peso': 4, 'valor': 3},
    {'item': 'item 6', 'peso': 12, 'valor': 11},
    {'item': 'item 7', 'peso': 5, 'valor': 2},
    {'item': 'item 8', 'peso': 13, 'valor': 7},
    {'item': 'item 9', 'peso': 3, 'valor': 4},
    {'item': 'item 10', 'peso': 9, 'valor': 7},
]

def funcaoFitness(genes, dados):
    pesoTotal = 0
    valorTotal = 0
    
    for i in range(len(genes)):

        if (genes[i] == 1):
            pesoTotal += dados[i]['peso']
            valorTotal += dados[i]['valor']
    
    if (pesoTotal <= 20):
        return valorTotal

    return 0

ag = AlgoritmoGenetico(dados, tamPopulacao=200, probMutacao=100, funcaoFitness=funcaoFitness)
ag.executa()
print(ag.populacao)
print(ag.melhorResultado())

