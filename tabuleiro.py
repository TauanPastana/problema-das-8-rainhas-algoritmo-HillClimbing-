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
    


print(funcao_objetiva([5,4,7,3,5,1,7,1]))
