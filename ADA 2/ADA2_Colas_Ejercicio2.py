class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def ver(self):
        return self.items


# Diccionario para las colas de cada servicio
servicios = {
    1: Cola(),  # Servicio 1
    2: Cola(),  # Servicio 2
    3: Cola()   # Servicio 3
}

# Contadores para llevar el número de atención por servicio
contador_servicio = {1: 0, 2: 0, 3: 0}

print("=== SISTEMA DE COLAS DE SERVICIOS ===")
print("Comandos:")
print("  C# → llega un cliente al servicio #")
print("  A# → atender cliente del servicio #")
print("  X  → salir del sistema")
print("--------------------------------------")

while True:
    entrada = input("Ingrese comando: ").strip().upper()

    if entrada == "X":
        print("Cerrando sistema...")
        break

    # Llegada de cliente
    elif entrada.startswith("C"):
        try:
            num_servicio = int(entrada[1:])
            if num_servicio in servicios:
                contador_servicio[num_servicio] += 1
                numero_atencion = contador_servicio[num_servicio]
                servicios[num_servicio].encolar(numero_atencion)
                print(f"Cliente agregado al servicio {num_servicio} con número {numero_atencion}")
            else:
                print("Servicio no válido.")
        except:
            print("Formato incorrecto. Usa C# (ej. C1).")

    # Atención de cliente
    elif entrada.startswith("A"):
        try:
            num_servicio = int(entrada[1:])
            if num_servicio in servicios:
                cliente = servicios[num_servicio].desencolar()
                if cliente is not None:
                    print(f"Atendiendo al cliente número {cliente} del servicio {num_servicio}")
                else:
                    print(f"No hay clientes en la cola del servicio {num_servicio}")
            else:
                print("Servicio no válido.")
        except:
            print("Formato incorrecto. Usa A# (ej. A2).")

    else:
        print("Comando no reconocido. Usa C#, A# o X.")
