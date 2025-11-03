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

def eliminar_repetidos_automatico(self):
    """2. Elimina de manera automática todos los elementos repetidos de POSTRES"""
    print("\n--- ELIMINACIÓN AUTOMÁTICA DE POSTRES REPETIDOS ---")
    
    if not self.POSTRES:
        print("No hay postres en el sistema.")
        return
    
    # Creamos un conjunto para trackear nombres únicos
    nombres_vistos = set()
    postres_unicos = []
    repetidos_eliminados = 0
    
    for postre in self.POSTRES:
        nombre = postre[0]  # nombre del postre
        
        if nombre not in nombres_vistos:
            nombres_vistos.add(nombre)
            postres_unicos.append(postre)
        else:
            print(f"Eliminando postre repetido: '{nombre}'")
            repetidos_eliminados += 1
    
    # Reemplazar la lista original
    self.POSTRES = postres_unicos
    
    if repetidos_eliminados == 0:
        print("No se encontraron postres repetidos en el sistema.")
    else:
        print(f"Se eliminaron {repetidos_eliminados} postres repetidos.")
    
    return repetidos_eliminados

# Agregar este método a la clase SistemaPostres
def agregar_metodo_eliminar_repetidos():
    # Agregamos el método a la clase (en una implementación real, esto iría dentro de la clase)
    SistemaPostres.eliminar_repetidos_automatico = eliminar_repetidos_automatico

# Demostración del funcionamiento
def demostrar_eliminacion_repetidos():
    sistema = SistemaPostres()
    agregar_metodo_eliminar_repetidos()
    
    print("=== DEMOSTRACIÓN ELIMINACIÓN DE REPETIDOS ===")
    
    # Crear postres con duplicados
    sistema.alta_postre("Tarta de Manzana", ["manzanas", "harina"])
    sistema.alta_postre("Flan", ["huevos", "leche"])
    sistema.alta_postre("Tarta de Manzana", ["manzanas", "canela"])  # DUPLICADO
    sistema.alta_postre("Brownie", ["chocolate", "harina"])
    sistema.alta_postre("Flan", ["huevos", "caramelo"])  # DUPLICADO
    sistema.alta_postre("Flan", ["huevos", "vainilla"])  # DUPLICADO
    
    print("\n--- Estado ANTES de eliminar repetidos ---")
    sistema.mostrar_postres()
    
    # Ejecutar eliminación automática
    sistema.eliminar_repetidos_automatico()
    
    print("\n--- Estado DESPUÉS de eliminar repetidos ---")
    sistema.mostrar_postres()

# Ejecutar la demostración
if __name__ == "__main__":
    demostrar_eliminacion_repetidos()
