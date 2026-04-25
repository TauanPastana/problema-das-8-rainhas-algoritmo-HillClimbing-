from random import randint

def random_tabuleiro():
    array = [0,0,0,0,0,0,0,0]

    for i in range(8):
      
        array[i] = randint(0,7)
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

def hill_climbing():
    estado_inicial = random_tabuleiro()
    h_atual = funcao_objetiva(estado_inicial) 
    print(f"Estado inicial: {estado_inicial} | com {funcao_objetiva(estado_inicial) } conflitos")
    estado_atual = estado_inicial.copy()
    cont = 0
    while h_atual != 0 and cont <=100000:
        cont+=1
        melhor_vizinho = estado_atual
        melhor_h = h_atual
    
        lista_vizinhaca = funcao_vizinhanca(estado_atual)
        for vizinho in lista_vizinhaca:
            h_vizinho = funcao_objetiva(vizinho)
            if melhor_h > h_vizinho:
                melhor_vizinho = vizinho
                melhor_h = h_vizinho
                continue
        if melhor_h < h_atual:
            estado_atual = melhor_vizinho
            h_atual = melhor_h

    if h_atual == 0:
        print("Motivo: Chegou em 0 conflitos!")
    else:
        print("Motivo: Passou do limite de iterações!")
    
    print(f"Estado atual: {estado_atual} | com {h_atual} conflitos")
    

hill_climbing()
            





     



    


