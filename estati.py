from statistics import mean, stdev
import json
import argparse
import os
from datetime import datetime
from hill import hill_climbing


def executar_experimentos(numero_execucoes=15, limite_iteracoes=1000, variante="subida_mais_ingreme"):
    resultados = []

    for execucao in range(1, numero_execucoes + 1):
        resultado = hill_climbing(
            limite_iteracoes=limite_iteracoes,
            variante=variante
        )
        resultado["execucao"] = execucao
        resultados.append(resultado)

    return resultados


def calcular_metricas(resultados):
    lista_iteracoes = [r["iteracoes"] for r in resultados]
    lista_tempos = [r["tempo_execucao"] for r in resultados]
    lista_h_finais = [r["funcao_objetivo_final"] for r in resultados]

    total_sucessos = sum(1 for r in resultados if r["sucesso"])
    total_otimos_platos = sum(
        1 for r in resultados
        if "plato" in r["classificacao"] or "otimo" in r["classificacao"]
    )

    metricas = {
        "numero_execucoes": len(resultados),
        "media_iteracoes": mean(lista_iteracoes) if lista_iteracoes else 0,
        "desvio_padrao_iteracoes": stdev(lista_iteracoes) if len(lista_iteracoes) > 1 else 0,
        "media_tempo_execucao": mean(lista_tempos) if lista_tempos else 0,
        "desvio_padrao_tempo_execucao": stdev(lista_tempos) if len(lista_tempos) > 1 else 0,
        "taxa_sucesso_percentual": (total_sucessos / len(resultados)) * 100 if resultados else 0,
        "valor_medio_final_funcao_objetivo": mean(lista_h_finais) if lista_h_finais else 0,
        "quantidade_sucessos": total_sucessos,
        "quantidade_otimos_locais_ou_platos": total_otimos_platos,
    }

    return metricas


def obter_cinco_melhores_solucoes_distintas(resultados):
    unicos = {}

    for r in resultados:
        chave = tuple(r["estado_final"])

        if chave not in unicos:
            unicos[chave] = r
        else:
            atual = unicos[chave]
            if r["funcao_objetivo_final"] < atual["funcao_objetivo_final"]:
                unicos[chave] = r

    lista = list(unicos.values())
    lista.sort(key=lambda x: (x["funcao_objetivo_final"], x["iteracoes"], x["tempo_execucao"]))
    return lista[:5]


def salvar_resultado_json(estrutura, diretorio_saida="saida", nome_arquivo=None):
    os.makedirs(diretorio_saida, exist_ok=True)

    if nome_arquivo is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"resultado.json"

    caminho_arquivo = os.path.join(diretorio_saida, nome_arquivo)

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(estrutura, f, ensure_ascii=False, indent=2)

    return caminho_arquivo


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--execucoes", type=int, default=15)
    parser.add_argument("--iteracoes", type=int, default=1000)
    parser.add_argument("--variante", type=str, default="subida_mais_ingreme")
    parser.add_argument("--saida", type=str, default="saida")
    parser.add_argument("--arquivo", type=str, default=None)
    args = parser.parse_args()

    resultados = executar_experimentos(
        numero_execucoes=args.execucoes,
        limite_iteracoes=args.iteracoes,
        variante=args.variante,
    )

    metricas = calcular_metricas(resultados)
    melhores_solucoes = obter_cinco_melhores_solucoes_distintas(resultados)

    estrutura = {
        "metricas": metricas,
        "resultados": resultados,
        "cinco_melhores_solucoes_distintas": melhores_solucoes,
    }

    caminho_salvo = salvar_resultado_json(
        estrutura=estrutura,
        diretorio_saida=args.saida,
        nome_arquivo=args.arquivo
    )

    print(f"Arquivo salvo em: {caminho_salvo}", flush=True)


if __name__ == "__main__":
    main()