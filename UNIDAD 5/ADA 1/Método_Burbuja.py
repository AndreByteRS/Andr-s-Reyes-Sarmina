# ORDENAMIENTO BURBUJA PASO A PASO

lista = list(map(int, input("Ingresa los números separados por espacio: ").split()))

n = len(lista)
paso = 1

print("\n--- ORDENAMIENTO BURBUJA ---\n")

for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
        print(f"Paso {paso}: {lista}")
        paso += 1

print("\nLista ordenada:", lista)
