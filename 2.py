import random

def verificar_condicoes(i, j, n):
    if i < n and j < n and i < j and n <= 100 and i >= 0 and j >= 0 and n >= 0:
        return True
    else:
        return False

def preencher_lista(n):
    lista = []
    for i in range(n):
        lista.append(random.uniform(0, 100))
    return lista

def trocar_elementos(lista, i, j, n):
    if verificar_condicoes(i, j, n):
        lista[i], lista[j] = lista[j], lista[i]
        return lista
    else:
        print("Valores inválidos na entrada de dados")
        return None

def main():
    i = int(input("Digite o valor de i: "))
    j = int(input("Digite o valor de j: "))
    n = int(input("Digite o valor de n: "))

    if verificar_condicoes(i, j, n):
        lista = preencher_lista(n)
        print("Lista preenchida:", lista)
        lista = trocar_elementos(lista, i, j, n)
        if lista:
            print("Lista após a troca:", lista)
    else:
        print("Valores inválidos na entrada de dados")

if __name__ == '__main__':
    main()