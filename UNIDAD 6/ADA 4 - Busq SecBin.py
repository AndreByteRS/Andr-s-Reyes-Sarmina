# busquedas.py
# Programa interactivo con 3 métodos de búsqueda:
# 1) Secuencial (linear)
# 2) Binaria
# 3) Hash (tabla simple con encadenamiento)
# Autor: ejemplo educativo
#Dada una carpeta con arcivos y quiero que esa carpeta la convierta a un Hash

from typing import List, Optional

def leer_lista_int(prompt="Ingresa números separados por espacios: ") -> List[int]:
    entrada = input(prompt).strip()
    if entrada == "":
        return []
    try:
        return [int(x) for x in entrada.split()]
    except ValueError:
        print("Entrada inválida. Intenta de nuevo con números separados por espacios.")
        return leer_lista_int(prompt)

# ---------- BÚSQUEDAS ----------
def busqueda_secuencial(arr: List[int], clave: int) -> Optional[int]:
    """Devuelve índice de la primera ocurrencia o None si no está."""
    for i, v in enumerate(arr):
        if v == clave:
            return i
    return None

def busqueda_binaria(arr: List[int], clave: int) -> Optional[int]:
    """Asume arr ordenado ascendentemente. Devuelve índice o None."""
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == clave:
            return medio
        elif arr[medio] < clave:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

# Implementación simple de tabla hash con encadenamiento
class TablaHash:
    def __init__(self, m=11):
        self.m = max(3, int(m))  # tamaño de la tabla
        self.tabla = [[] for _ in range(self.m)]

    def _hash(self, clave: int) -> int:
        # función hash simple: módulo
        return clave % self.m

    def insertar(self, clave: int):
        idx = self._hash(clave)
        bucket = self.tabla[idx]
        if clave not in bucket:
            bucket.append(clave)

    def buscar(self, clave: int) -> Optional[int]:
        idx = self._hash(clave)
        bucket = self.tabla[idx]
        # devolvemos índice conceptual: (idx, posición_en_bucket)
        if clave in bucket:
            return idx  # retornamos el índice de la casilla hash (útil para entender)
        return None

    def __str__(self):
        s = []
        for i, bucket in enumerate(self.tabla):
            s.append(f"{i}: {bucket}")
        return "\n".join(s)

# ---------- EJERCICIOS (scenarios) ----------
def ejercicio_secuencial():
    print("\nEJERCICIO 1 - BÚSQUEDA SECUENCIAL")
    print("Contexto: lista de IDs de estudiantes (no ordenada).")
    arr = leer_lista_int("Introduce los IDs (ej: 101 203 150 99 305): ")
    if not arr:
        print("Lista vacía. Regresando al menú.")
        return
    clave = int(input("Introduce el ID a buscar: "))
    idx = busqueda_secuencial(arr, clave)
    if idx is not None:
        print(f"Encontrado: ID {clave} en la posición (índice) {idx}.")
    else:
        print(f"No se encontró el ID {clave} en la lista.")

def ejercicio_binaria():
    print("\nEJERCICIO 2 - BÚSQUEDA BINARIA")
    print("Contexto: lista ordenada de calificaciones. (Se ordenará automáticamente)")
    arr = leer_lista_int("Introduce las calificaciones (ej: 55 70 100 80 90): ")
    if not arr:
        print("Lista vacía. Regresando al menú.")
        return
    arr.sort()
    print(f"Lista ordenada: {arr}")
    clave = int(input("Introduce la calificación a buscar: "))
    idx = busqueda_binaria(arr, clave)
    if idx is not None:
        print(f"Encontrado: {clave} en la posición (índice) {idx} de la lista ordenada.")
    else:
        print(f"No se encontró la calificación {clave}.")

def ejercicio_hash():
    print("\nEJERCICIO 3 - BÚSQUEDA CON HASH")
    print("Contexto: registro de empleados por su número. Usamos una tabla hash simple.")
    arr = leer_lista_int("Introduce los números de empleado (ej: 12 34 56 78 90): ")
    if not arr:
        print("Lista vacía. Regresando al menú.")
        return
    # Pedimos tamaño de tabla opcional
    try:
        m = int(input("Tamaño de la tabla hash (presiona Enter para usar 11): ") or 11)
    except ValueError:
        m = 11
    tabla = TablaHash(m=m)
    for v in arr:
        tabla.insertar(v)
    print("\nTabla hash construida (index : bucket):")
    print(tabla)
    clave = int(input("Introduce el número de empleado a buscar: "))
    idx = tabla.buscar(clave)
    if idx is not None:
        print(f"Encontrado: {clave} en la casilla hash {idx}.")
    else:
        print(f"No se encontró {clave} en la tabla hash.")

# ---------- MENÚ ----------
def menu():
    opciones = {
        "1": ejercicio_secuencial,
        "2": ejercicio_binaria,
        "3": ejercicio_hash,
        "4": lambda: print("Saliendo..."),
    }
    while True:
        print("\n=== MENÚ DE BÚSQUEDAS ===")
        print("1) Ejercicio: Búsqueda secuencial")
        print("2) Ejercicio: Búsqueda binaria")
        print("3) Ejercicio: Búsqueda con tabla hash")
        print("4) Salir")
        opcion = input("Elige una opción (1-4): ").strip()
        if opcion not in opciones:
            print("Opción inválida. Intenta de nuevo.")
            continue
        if opcion == "4":
            opciones[opcion]()
            break
        opciones[opcion]()

if __name__ == "__main__":
    menu()
