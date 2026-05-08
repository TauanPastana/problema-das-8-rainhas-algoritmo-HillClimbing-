from random import randint
from time import perf_counter

def gerar_estado_inicial():
    return [randint(0, 7) for _ in range(8)]

def funcao_objetivo(estado):
    conflitos = 0
    n = len(estado)

    for i in range(n):
        for j in range(i + 1, n):
            mesma_linha = estado[i] == estado[j]
            mesma_diagonal = abs(estado[i] - estado[j]) == abs(i - j)

            if mesma_linha or mesma_diagonal:
                conflitos += 1

    return conflitos

def funcao_vizinhanca(estado_atual):
    lista_vizinhanca = []

    for coluna in range(len(estado_atual)):
        for linha in range(8):
            if estado_atual[coluna] == linha:
                continue
            vizinho = estado_atual.copy()
            vizinho[coluna] = linha
            lista_vizinhanca.append(vizinho)

    return lista_vizinhanca

def hill_climbing(limite_iteracoes=1000):
    estado_inicial = gerar_estado_inicial()
    estado_atual = estado_inicial.copy()
    h_atual = funcao_objetivo(estado_atual)

    iteracoes = 0
    inicio = perf_counter()

    while h_atual > 0 and iteracoes < limite_iteracoes:
        iteracoes += 1
        melhor_vizinho = estado_atual
        melhor_h = h_atual

        for vizinho in funcao_vizinhanca(estado_atual):
            h_vizinho = funcao_objetivo(vizinho)
            if h_vizinho < melhor_h:
                melhor_vizinho = vizinho
                melhor_h = h_vizinho

        if melhor_h < h_atual:
            estado_atual = melhor_vizinho
            h_atual = melhor_h
        else:
            break

    tempo_execucao = perf_counter() - inicio
    sucesso = (h_atual == 0)

    if sucesso:
        motivo = "Chegou em 0 conflitos"
    elif iteracoes >= limite_iteracoes:
        motivo = "Atingiu o limite de iterações"
    else:
        motivo = "Não encontrou vizinho melhor, possivel ótimo local ou platô"

    resultado = {
        "estado_inicial": estado_inicial,
        "estado_final": estado_atual,
        "conflitos_finais": h_atual,
        "iteracoes": iteracoes,
        "tempo_execucao": tempo_execucao,
        "sucesso": sucesso,
        "motivo_parada": motivo
    }

    return resultado

resultado = hill_climbing(limite_iteracoes=1000)
print(resultado)