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

def hill_climbing():
    estado_inicial = random_tabuleiro()
    menor_h = funcao_objetiva(estado_inicial) 
    print(f"Estado inicial: {estado_inicial} | com {menor_h} conflitos")
    estado_atual = estado_inicial.copy()
    cont = 0
    while menor_h != 0 and cont <=50000:
    
        lista_vizinhaca = funcao_vizinhanca(estado_atual)
        for vizinho in lista_vizinhaca:
            cont+=1
            h_vizinho = funcao_objetiva(vizinho)
            if h_vizinho == 0:
                menor_h = h_vizinho
                estado_atual = vizinho
                break
            if menor_h > h_vizinho:
                estado_atual = vizinho
                menor_h = h_vizinho
                continue


                
                

    print(f"Estado atual: {estado_atual} | com {menor_h} conflitos")
    
    # for vizinho in lista_vizinhaca:
    #     if menor_h != 0:
    #         h_vizinho = funcao_objetiva(vizinho)
    #         if menor_h > h_vizinho:
    #             estado_atual = vizinho
    #             menor_h = h_vizinho
    #     else:
    #         break
    
    # return estado_atual

hill_climbing()
            





     



    


