
# Clase base que representa un vehículo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca  # Atributo privado (encapsulación)
        self.__modelo = modelo
        self.año = año

    # Método público para obtener información del vehículo
    def obtener_informacion(self):
        return f"{self.__marca} {self.__modelo} ({self.año})"

    # Método para describir el uso del vehículo
    def uso(self):
        return "Este es un vehículo genérico."

# Clase derivada que representa un automóvil, hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)  # Llama al constructor de la clase base
        self.puertas = puertas

    # Sobrescribe el método uso para demostrar polimorfismo
    def uso(self):
        return f"Este automóvil es ideal para uso personal y tiene {self.puertas} puertas."

# Clase derivada que representa una motocicleta, hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo

    # Sobrescribe el método uso para demostrar polimorfismo
    def uso(self):
        return f"Esta motocicleta tipo {self.tipo} es ideal para viajes rápidos."

# Función principal para demostrar el funcionamiento
def main():
    # Crear instancias de las clases
    vehiculo_generico = Vehiculo("Genérico", "ModeloX", 2020)
    automovil = Automovil("Toyota", "Corolla", 2022, 4)
    motocicleta = Motocicleta("Yamaha", "YZF-R3", 2021, "deportiva")

    # Demostrar encapsulación y uso de métodos
    print(vehiculo_generico.obtener_informacion())
    print(vehiculo_generico.uso())

    print(automovil.obtener_informacion())
    print(automovil.uso())

    print(motocicleta.obtener_informacion())
    print(motocicleta.uso())

if __name__ == "__main__":
    main()
