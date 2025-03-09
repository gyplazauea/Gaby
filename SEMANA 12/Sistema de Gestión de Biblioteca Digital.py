class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.datos[0]} - {self.datos[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = set()  # Conjunto para IDs de usuario únicos
        self.historial_prestamos = {}

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.user_id)
            self.historial_prestamos[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_de_baja_usuario(self, user_id):
        if user_id in self.usuarios_registrados:
            usuario = self.historial_prestamos[user_id]
            if usuario.libros_prestados:
                print("No se puede eliminar al usuario porque tiene libros prestados.")
            else:
                self.usuarios_registrados.remove(user_id)
                del self.historial_prestamos[user_id]
                print("Usuario eliminado correctamente.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.historial_prestamos[user_id]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro prestado: {libro} a {usuario}")
        else:
            print("Usuario no registrado o libro no disponible.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios_registrados:
            usuario = self.historial_prestamos[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro devuelto: {libro}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no registrado.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros_disponibles.values():
            if (titulo and titulo.lower() in libro.datos[0].lower()) or \
                    (autor and autor.lower() in libro.datos[1].lower()) or \
                    (categoria and categoria.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios_registrados:
            usuario = self.historial_prestamos[user_id]
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado.")
            return []


# Pruebas
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "12345")
libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", "67890")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuario
usuario1 = Usuario("Juan Pérez", "001")
biblioteca.registrar_usuario(usuario1)

# Prestar libro
biblioteca.prestar_libro("001", "12345")

# Devolver libro
biblioteca.devolver_libro("001", "12345")

# Buscar libro por título
resultados = biblioteca.buscar_libro(titulo="1984")
print("Resultados de búsqueda:", resultados)

# Listar libros prestados
total_prestados = biblioteca.listar_libros_prestados("001")
print("Libros prestados:", total_prestados)
