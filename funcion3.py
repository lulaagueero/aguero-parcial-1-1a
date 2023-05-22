#lucia agüero parcial 1A
def ordenarCaracteres(texto:str):
    tam = len(texto)
    for i in range(tam - 1):
        for j in range(i+i, tam):
            if (texto[i] > texto[j]):
                aux = texto[i]
                texto[i] = texto[j]
                texto[j] = aux
    print(texto)

ordenarCaracteres("algoritmo")