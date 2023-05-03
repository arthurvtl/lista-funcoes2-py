import random

# Função que preenche a lista com valores aleatórios
def preencher_lista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(1, 10))
    return lista

# Função que acumula os valores da lista
def acumular_valores(lista):
    for i in range(1, len(lista)):
        lista[i] += lista[i-1]
    return lista

# Programa principal
n = int(input("Digite o tamanho da lista: "))
lista = preencher_lista(n)

print("Lista original:", lista)
lista_acumulada = acumular_valores(lista)
print("Lista acumulada:", lista_acumulada)