import os
import json

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario si existe."""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r") as file:
                    self.productos = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al cargar el inventario: {e}")
            self.productos = {}
        except PermissionError:
            print("No tienes permiso para acceder al archivo de inventario.")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, "w") as file:
                json.dump(self.productos, file, indent=4)
        except PermissionError:
            print("No tienes permiso para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        """Añade un nuevo producto al inventario."""
        self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado correctamente.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """Actualiza los datos de un producto existente."""
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre]["cantidad"] = cantidad
            if precio is not None:
                self.productos[nombre]["precio"] = precio
            self.guardar_inventario()
            print(f"Producto '{nombre}' actualizado correctamente.")
        else:
            print("El producto no existe en el inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado correctamente.")
        else:
            print("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            for nombre, datos in self.productos.items():
                print(f"{nombre}: Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")
        else:
            print("El inventario está vacío.")

# Ejemplo de uso
def main():
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto\n2. Actualizar producto\n3. Eliminar producto\n4. Mostrar inventario\n5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no se cambia): ")
            precio = input("Nuevo precio (dejar vacío si no se cambia): ")
            inventario.actualizar_producto(nombre, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
