import random

def preencher_lista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0, 100))
    return lista, []

def ordenar_lista(lista_original):
    lista_ordenada = []
    for i in range(len(lista_original)):
        for j in range(len(lista_ordenada)):
            if lista_original[i] < lista_ordenada[j]:
                lista_ordenada.insert(j, lista_original[i])
                break
        else:
            lista_ordenada.append(lista_original[i])
    return lista_ordenada

# Programa principal
n = int(input("Digite o tamanho da lista: "))
lista_original, lista_ordenada = preencher_lista(n)

print("Lista original:", lista_original)
lista_ordenada = ordenar_lista(lista_original)
print("Lista ordenada:", lista_ordenada)