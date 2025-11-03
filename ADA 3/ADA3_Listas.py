class SistemaPostres:
    def __init__(self):
        # Arreglo de postres ordenado alfabéticamente
        # Cada elemento es una tupla: (nombre_postre, lista_ingredientes)
        self.POSTRES = []
    
    def _buscar_postre(self, nombre_postre):
        """Busca un postre en el arreglo y retorna su índice y datos"""
        for i, (nombre, ingredientes) in enumerate(self.POSTRES):
            if nombre == nombre_postre:
                return i, nombre, ingredientes
        return -1, None, None
    
    def _insertar_ordenado(self, nombre_postre, ingredientes):
        """Inserta un postre manteniendo el orden alfabético"""
        nuevo_postre = (nombre_postre, ingredientes)
        
        if not self.POSTRES:
            self.POSTRES.append(nuevo_postre)
            return
        
        # Buscar la posición correcta para insertar
        for i, (nombre, _) in enumerate(self.POSTRES):
            if nombre_postre < nombre:
                self.POSTRES.insert(i, nuevo_postre)
                return
        
        # Si llegamos aquí, va al final
        self.POSTRES.append(nuevo_postre)
    
    # a. Dado el nombre de un postre, imprima la lista de todos sus ingredientes
    def imprimir_ingredientes(self, nombre_postre):
        """a. Imprime la lista de ingredientes de un postre"""
        indice, nombre, ingredientes = self._buscar_postre(nombre_postre)
        
        if indice == -1:
            print(f"Error: El postre '{nombre_postre}' no existe en el sistema.")
            return False
        else:
            print(f"\nIngredientes de '{nombre}':")
            if not ingredientes:
                print("  No tiene ingredientes registrados.")
            else:
                for i, ingrediente in enumerate(ingredientes, 1):
                    print(f"  {i}. {ingrediente}")
            return True
    
    # b. Dado el nombre de un postre, inserte nuevos ingredientes a su correspondiente lista
    def insertar_ingredientes(self, nombre_postre, nuevos_ingredientes):
        """b. Inserta nuevos ingredientes a un postre existente"""
        indice, nombre, ingredientes = self._buscar_postre(nombre_postre)
        
        if indice == -1:
            print(f"Error: El postre '{nombre_postre}' no existe en el sistema.")
            return False
        else:
            # Convertir a lista si es un solo ingrediente
            if isinstance(nuevos_ingredientes, str):
                nuevos_ingredientes = [nuevos_ingredientes]
            
            # Agregar ingredientes que no existan ya
            ingredientes_existentes = set(ingredientes)
            nuevos = [ing for ing in nuevos_ingredientes if ing not in ingredientes_existentes]
            
            if not nuevos:
                print(f"Todos los ingredientes ya existen en '{nombre}'")
                return True
            
            ingredientes.extend(nuevos)
            self.POSTRES[indice] = (nombre, ingredientes)
            print(f"Se agregaron {len(nuevos)} ingredientes a '{nombre}': {', '.join(nuevos)}")
            return True
    
    # c. Dado el nombre de un postre, elimine alguno de sus ingredientes
    def eliminar_ingrediente(self, nombre_postre, ingrediente_eliminar):
        """c. Elimina un ingrediente de un postre"""
        indice, nombre, ingredientes = self._buscar_postre(nombre_postre)
        
        if indice == -1:
            print(f"Error: El postre '{nombre_postre}' no existe en el sistema.")
            return False
        
        if ingrediente_eliminar not in ingredientes:
            print(f"Error: El ingrediente '{ingrediente_eliminar}' no existe en '{nombre}'")
            return False
        
        ingredientes.remove(ingrediente_eliminar)
        self.POSTRES[indice] = (nombre, ingredientes)
        print(f"Se eliminó el ingrediente '{ingrediente_eliminar}' de '{nombre}'")
        return True
    
    # d. Dé de alta un postre con todos sus ingredientes
    def alta_postre(self, nombre_postre, ingredientes=None):
        """d. Da de alta un nuevo postre con sus ingredientes"""
        indice, nombre, _ = self._buscar_postre(nombre_postre)
        
        if indice != -1:
            print(f"Error: El postre '{nombre_postre}' ya existe en el sistema.")
            return False
        
        # Si no se proporcionan ingredientes, crear lista vacía
        if ingredientes is None:
            ingredientes = []
        
        # Convertir a lista si es un solo ingrediente
        if isinstance(ingredientes, str):
            ingredientes = [ingredientes]
        
        self._insertar_ordenado(nombre_postre, ingredientes)
        print(f"Postre '{nombre_postre}' dado de alta exitosamente con {len(ingredientes)} ingredientes.")
        return True
    
    # e. Dé de baja un postre con todos sus ingredientes
    def baja_postre(self, nombre_postre):
        """e. Da de baja un postre y todos sus ingredientes"""
        indice, nombre, ingredientes = self._buscar_postre(nombre_postre)
        
        if indice == -1:
            print(f"Error: El postre '{nombre_postre}' no existe en el sistema.")
            return False
        
        self.POSTRES.pop(indice)
        print(f"Postre '{nombre}' eliminado exitosamente junto con sus {len(ingredientes)} ingredientes.")
        return True
    
    # Método auxiliar para mostrar todos los postres
    def mostrar_postres(self):
        """Muestra todos los postres en el sistema"""
        if not self.POSTRES:
            print("No hay postres en el sistema.")
            return
        
        print("\n=== POSTRES EN EL SISTEMA ===")
        for nombre, ingredientes in self.POSTRES:
            print(f"{nombre}: {len(ingredientes)} ingredientes")
            if ingredientes:
                print(f"  → {', '.join(ingredientes)}")

# Función para demostrar el sistema
def demostrar_sistema():
    sistema = SistemaPostres()
    
    print("=== SISTEMA DE GESTIÓN DE POSTRES ===")
    
    # d. Dar de alta algunos postres
    print("\n--- d. Dando de alta postres ---")
    sistema.alta_postre("Tarta de Manzana", ["manzanas", "harina", "azúcar", "mantequilla", "canela"])
    sistema.alta_postre("Flan", ["huevos", "leche", "azúcar", "vainilla"])
    sistema.alta_postre("Brownie", ["chocolate", "harina", "huevos", "mantequilla", "nueces"])
    sistema.alta_postre("Mousse de Chocolate", ["chocolate", "crema", "huevos", "azúcar"])
    
    # Mostrar estado inicial
    sistema.mostrar_postres()
    
    # a. Imprimir ingredientes de un postre
    print("\n--- a. Imprimir ingredientes ---")
    sistema.imprimir_ingredientes("Flan")
    sistema.imprimir_ingredientes("Postre Inexistente")  # Caso de error
    
    # b. Insertar nuevos ingredientes
    print("\n--- b. Insertar ingredientes ---")
    sistema.insertar_ingredientes("Flan", "caramelo")  # Ingrediente único
    sistema.insertar_ingredientes("Tarta de Manzana", ["limón", "nuez moscada"])  # Múltiples ingredientes
    sistema.insertar_ingredientes("Tarta de Manzana", "manzanas")  # Ingrediente duplicado
    sistema.insertar_ingredientes("Postre Inexistente", "ingrediente")  # Postre no existe
    
    sistema.imprimir_ingredientes("Flan")
    
    # c. Eliminar ingredientes
    print("\n--- c. Eliminar ingredientes ---")
    sistema.eliminar_ingrediente("Flan", "caramelo")
    sistema.eliminar_ingrediente("Flan", "ingrediente_inexistente")  # Ingrediente no existe
    sistema.eliminar_ingrediente("Postre Inexistente", "algo")  # Postre no existe
    
    sistema.imprimir_ingredientes("Flan")
    
    # e. Dar de baja un postre
    print("\n--- e. Dar de baja postre ---")
    sistema.baja_postre("Brownie")
    sistema.baja_postre("Postre Inexistente")  # Caso de error
    
    # Mostrar estado final
    print("\n--- Estado final del sistema ---")
    sistema.mostrar_postres()
    
    # Casos especiales
    print("\n--- Casos especiales ---")
    # Postre sin ingredientes
    sistema.alta_postre("Gelatina")
    sistema.imprimir_ingredientes("Gelatina")
    
    # Insertar múltiples ingredientes a postre vacío
    sistema.insertar_ingredientes("Gelatina", ["gelatina en polvo", "agua", "azúcar"])
    sistema.imprimir_ingredientes("Gelatina")

if __name__ == "__main__":
    demostrar_sistema()
