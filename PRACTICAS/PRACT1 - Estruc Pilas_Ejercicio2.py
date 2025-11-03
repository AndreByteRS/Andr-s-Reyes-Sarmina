class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        return self.items.pop() if self.items else None
    
    def __str__(self):
        return f"{self.nombre}: {self.items}"


def mover_discos(n, origen, destino, auxiliar):
    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mover disco {disco} de {origen.nombre} a {destino.nombre}")
    else:
        mover_discos(n-1, origen, auxiliar, destino)
        mover_discos(1, origen, destino, auxiliar)
        mover_discos(n-1, auxiliar, destino, origen)


# Ejemplo con 3 discos
origen = Pila("Origen")
auxiliar = Pila("Auxiliar")
destino = Pila("Destino")

# Apilar discos en la torre de origen (3 -> más grande abajo, 1 -> más pequeño arriba)
for disco in range(3, 0, -1):
    origen.apilar(disco)

print("Estado inicial:")
print(origen, auxiliar, destino, "\n")

mover_discos(3, origen, destino, auxiliar)

print("\nEstado final:")
print(origen, auxiliar, destino)
