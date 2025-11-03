class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar_cola(self):
        if self.esta_vacia():
            return "Vacía"
        return ", ".join(self.items)


class SistemaColasConsola:
    def __init__(self):
        self.prefijos = {1: "CD", 2: "CE", 3: "CF"}
        self.colas = {1: Cola(), 2: Cola(), 3: Cola()}
        self.contadores = {1: 0, 2: 0, 3: 0}

    def generar_codigo_cliente(self, servicio):
        self.contadores[servicio] += 1
        numero = f"{self.contadores[servicio]:02d}"  # Dos dígitos
        codigo = f"{self.prefijos[servicio]}{numero}"  # Ejemplo: CD01, CE02, CF03
        self.colas[servicio].encolar(codigo)
        return codigo

    def llegada_cliente(self):
        try:
            servicio = int(input("Ingrese número de servicio (1, 2 o 3): "))
            if servicio not in self.colas:
                print("⚠️ Servicio inválido.")
                return
            codigo = self.generar_codigo_cliente(servicio)
            print(f"✅ Cliente agregado al servicio {servicio}: {codigo}")
            self.mostrar_colas()
        except ValueError:
            print("⚠️ Entrada inválida, ingrese un número.")

    def atender_cliente(self):
        try:
            servicio = int(input("Ingrese número de servicio (1, 2 o 3): "))
            if servicio not in self.colas:
                print("⚠️ Servicio inválido.")
                return
            if self.colas[servicio].esta_vacia():
                print(f"🚫 No hay clientes en la cola del servicio {servicio}.")
            else:
                codigo = self.colas[servicio].desencolar()
                print(f"👨‍💼 Atendiendo cliente {codigo} del servicio {servicio}.")
            self.mostrar_colas()
        except ValueError:
            print("⚠️ Entrada inválida, ingrese un número.")

    def mostrar_colas(self):
        print("\n📋 Estado actual de las colas:")
        for servicio in self.colas:
            print(f"  Servicio {servicio}: {self.colas[servicio].mostrar_cola()}")
        print("-" * 50)

    def ejecutar(self):
        print("=== Sistema de Atención de Clientes ===")
        while True:
            print("\nOpciones:")
            print("1. Agregar cliente")
            print("2. Atender cliente")
            print("3. Mostrar colas")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.llegada_cliente()
            elif opcion == "2":
                self.atender_cliente()
            elif opcion == "3":
                self.mostrar_colas()
            elif opcion == "4":
                print("👋 Saliendo del sistema...")
                break
            else:
                print("⚠️ Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    sistema = SistemaColasConsola()
    sistema.ejecutar()
