# Implementación sencilla de una Linked List en Python

# Clase Nodo: representa cada elemento de la lista
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Apunta al siguiente nodo


# Clase LinkedList: administra la lista completa
class LinkedList:
    def __init__(self):
        self.cabeza = None  # Primer nodo de la lista

    # Método para verificar si la lista está vacía
    def esta_vacia(self):
        return self.cabeza is None

    # Método para agregar un nuevo nodo al final
    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Método para eliminar un nodo por su valor
    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Elemento eliminado
            anterior = actual
            actual = actual.siguiente
        return False  # No se encontró el dato

    # Método para buscar un valor en la lista
    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    # Método para mostrar los elementos de la lista
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")


# Ejemplo de uso
if __name__ == "__main__":
    lista = LinkedList()

    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)
    lista.mostrar()  # 10 -> 20 -> 30 -> None

    lista.eliminar(20)
    lista.mostrar()  # 10 -> 30 -> None

    print("¿Está 30 en la lista?", lista.buscar(30))  # True
    print("¿Está 50 en la lista?", lista.buscar(50))  # False
