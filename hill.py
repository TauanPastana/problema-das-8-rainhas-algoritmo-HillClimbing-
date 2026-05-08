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


def hill_climbing(limite_iteracoes=1000, variante="subida_mais_ingreme"):
    estado_inicial = gerar_estado_inicial()
    estado_atual = estado_inicial.copy()
    h_atual = funcao_objetivo(estado_atual)

    iteracoes = 0
    inicio = perf_counter()
    houve_melhora = False

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
            houve_melhora = True
        else:
            break

    tempo_execucao = perf_counter() - inicio
    sucesso = h_atual == 0

    if sucesso:
        motivo_parada = "Chegou em h = 0"
        classificacao = "sucesso"
    elif iteracoes >= limite_iteracoes:
        motivo_parada = "Atingiu o limite de iteracoes"
        classificacao = "limite_iteracoes"
    else:
        motivo_parada = "Parou sem encontrar vizinho melhor"
        classificacao = "otimo_local_ou_plato" if houve_melhora else "plato_inicial_ou_otimo_local"

    return {
        "estado_inicial": estado_inicial,
        "estado_final": estado_atual,
        "iteracoes": iteracoes,
        "tempo_execucao": tempo_execucao,
        "funcao_objetivo_inicial": funcao_objetivo(estado_inicial),
        "funcao_objetivo_final": h_atual,
        "sucesso": sucesso,
        "motivo_parada": motivo_parada,
        "classificacao": classificacao,
        "variante": variante,
    }


if __name__ == "__main__":
    resultado = hill_climbing()
    print(resultado)