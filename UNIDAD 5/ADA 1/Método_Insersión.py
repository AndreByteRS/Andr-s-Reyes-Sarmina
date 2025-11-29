# ORDENAMIENTO POR INSERCIÓN PASO A PASO

lista = list(map(int, input("Ingresa los números separados por espacio: ").split()))

print("\n--- ORDENAMIENTO POR INSERCIÓN ---\n")

paso = 1

for i in range(1, len(lista)):
    clave = lista[i]
    j = i - 1

    while j >= 0 and lista[j] > clave:
        lista[j + 1] = lista[j]
        j -= 1

        print(f"Paso {paso}: {lista}")
        paso += 1

    lista[j + 1] = clave
    print(f"Paso {paso}: {lista}")
    paso += 1

print("\nLista ordenada:", lista)
