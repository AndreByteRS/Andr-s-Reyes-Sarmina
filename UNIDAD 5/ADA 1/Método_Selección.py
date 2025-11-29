# ORDENAMIENTO POR SELECCIÓN PASO A PASO

lista = list(map(int, input("Ingresa los números separados por espacio: ").split()))

print("\n--- ORDENAMIENTO POR SELECCIÓN ---\n")

paso = 1
n = len(lista)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if lista[j] < lista[min_index]:
            min_index = j

    lista[i], lista[min_index] = lista[min_index], lista[i]

    print(f"Paso {paso}: {lista}")
    paso += 1

print("\nLista ordenada:", lista)
