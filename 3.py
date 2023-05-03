import random
import math

def preenche_lista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(1,100))
    return lista

def calcula_desvio_padrao(lista, n):
    media = sum(lista)/n
    soma = 0
    for i in range(n):
        soma += (lista[i] - media)**2
    desvio_padrao = math.sqrt(soma/n)
    return desvio_padrao

# programa principal
n = int(input("Digite o tamanho da lista: "))
lista = preenche_lista(n)
print("Lista gerada:", lista)
desvio_padrao = calcula_desvio_padrao(lista, n)
print("Desvio padrão:", desvio_padrao)