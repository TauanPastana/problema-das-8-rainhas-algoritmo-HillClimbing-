from random import randint

def random_tabuleiro():
    array = [0,0,0,0,0,0,0,0]

    for i in range(8):
      
        array[i] = randint(0,8)
    return array

def funcao_objetiva(estado:list):
    conflitos = 0
    n = len(estado)

    for i in range(n):
        for j in range(i + 1, n):
            mesma_linha = estado[i] == estado[j]
            mesma_diagonal = abs(estado[i] - estado[j]) == abs(i - j)

            if mesma_linha or mesma_diagonal:
                conflitos += 1

    return conflitos

def funcao_vizinhanca(estado_atual:list) -> list:
    lista_vizinhaca = []
    for i in range(len(estado_atual)):
        for j in range(len(estado_atual)):
            vizinho = estado_atual.copy()
            if estado_atual[i] == j:
                continue
            vizinho[i] = j
            lista_vizinhaca.append(vizinho)
    
    return lista_vizinhaca




     



    


