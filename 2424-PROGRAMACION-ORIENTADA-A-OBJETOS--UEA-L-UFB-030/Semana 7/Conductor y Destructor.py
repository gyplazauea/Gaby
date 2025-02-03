class ArchivoTemporal:
    """
    Clase que simula la creación, uso y eliminación de un archivo temporal.
    """
    def __init__(self, nombre):
        """
        Constructor de la clase.
        Inicializa el nombre del archivo y simula la creación del archivo.
        """
        self.nombre = nombre
        print(f"Archivo temporal '{self.nombre}' creado.")

    def escribir(self, contenido):
        """
        Método para simular la escritura en el archivo.
        """
        print(f"Escribiendo en el archivo '{self.nombre}': {contenido}")

    def __del__(self):
        """
        Destructor de la clase.
        Simula la eliminación del archivo temporal.
        """
        print(f"Archivo temporal '{self.nombre}' eliminado.")


# Demostración del uso de la clase
if __name__ == "__main__":
    print("Inicio del programa.")
    # Crear un objeto de la clase ArchivoTemporal
    archivo = ArchivoTemporal("temp.txt")
    archivo.escribir("Este es un archivo temporal.")
    # Al finalizar el bloque o programa, el destructor se llama automáticamente.
    print("Fin del programa.")