class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Agrega un elemento a la pila"""
        self.items.append(item)

    def pop(self):
        """Elimina y devuelve el último elemento agregado"""
        if not self.is_empty():
            return self.items.pop()
        return "La pila está vacía"

    def peek(self):
        """Muestra el elemento en el tope sin eliminarlo"""
        if not self.is_empty():
            return self.items[-1]
        return "La pila está vacía"

    def is_empty(self):
        """Verifica si la pila está vacía"""
        return len(self.items) == 0

    def size(self):
        """Devuelve el tamaño de la pila"""
        return len(self.items)


# Ejemplo de uso
pila = Pila()
pila.push(10)
pila.push(20)
pila.push(30)

print("Elemento en el tope:", pila.peek())  # 30
print("Eliminando:", pila.pop())            # 30
print("Nuevo tope:", pila.peek())           # 20
print("Tamaño actual:", pila.size())        # 2
