import random

def preencher_lista(n):
    lista = []
    for i in range(n):
        lista.append(random.uniform(0, 10))
    return lista

def calcular_media_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)
    media = sum(lista_ordenada) / tamanho
    if tamanho % 2 == 0:
        mediana = (lista_ordenada[tamanho//2] + lista_ordenada[(tamanho//2)-1]) / 2
    else:
        mediana = lista_ordenada[tamanho//2]
    return media, mediana

n = int(input("Digite a quantidade de valores a serem gerados: "))
lista = preencher_lista(n)
media, mediana = calcular_media_mediana(lista)
print("Lista gerada:", lista)
print("Média:", media)
print("Mediana:", mediana)