#Clase Libro: Define los atributos del libro y un método para representar el libro como
# una cadena
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"
#Clase Usuario: Define los atributos del usuario, métodos para prestar y devolver libros,
# y listar los libros prestados.
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        return [str(libro) for libro in self.libros_prestados]
#Clase Biblioteca: Administra libros y usuarios, y proporciona métodos para añadir/quitar libros, registrar/dar de baja usuarios,
# prestar/devolver libros, buscar libros y listar libros prestados.
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.usuarios_ids = set()

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario in self.usuarios_ids:
            print("El ID de usuario ya está registrado.")
        else:
            usuario = Usuario(nombre, id_usuario)
            self.usuarios[id_usuario] = usuario
            self.usuarios_ids.add(id_usuario)
            print(f"Usuario '{nombre}' registrado con ID {id_usuario}.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.usuarios_ids.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros:
            print("El libro no está disponible en la biblioteca.")
            return
        if id_usuario not in self.usuarios:
            print("El usuario no está registrado.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        usuario.prestar_libro(libro)
        del self.libros[isbn]
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            print("El usuario no está registrado.")
            return
        if isbn in self.libros:
            print("El libro ya está en la biblioteca.")
            return
#creamos los usuarios
        usuario = self.usuarios[id_usuario]
        libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
        if libro:
            usuario.devolver_libro(libro)
            self.libros[isbn] = libro
            print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
        else:
            print("El usuario no tiene este libro.")
# creamos para buscar los libros
    def buscar_libro(self, busqueda):
        resultados = [str(libro) for libro in self.libros.values() if (
            busqueda.lower() in libro.titulo.lower() or
            busqueda.lower() in libro.autor.lower() or
            busqueda.lower() in libro.categoria.lower()
        )]
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.listar_libros_prestados()
        else:
            print("El usuario no está registrado.")
            return []
# Crear una instancia de la biblioteca
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "1234567890")
libro2 = Libro("1984", "George Orwell", "Distopía", "0987654321")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
biblioteca.registrar_usuario("Alice", "user1")
biblioteca.registrar_usuario("Bob", "user2")

# Prestar libros
biblioteca.prestar_libro("1234567890", "user1")

# Buscar libros
print("Resultados de búsqueda de 'Novela':")
print("\n".join(biblioteca.buscar_libro("Novela")))

# Listar libros prestados
print("Libros prestados por 'user1':")
print("\n".join(biblioteca.listar_libros_prestados("user1")))

# Devolver libro
biblioteca.devolver_libro("1234567890", "user1")

# Eliminar libros y usuarios
biblioteca.quitar_libro("0987654321")
biblioteca.dar_de_baja_usuario("user2")

# Mostrar estado final
print("Estado final de la biblioteca:")
print("\nLibros disponibles:")
for libro in biblioteca.libros.values():
    print(libro)
print("\nUsuarios registrados:")
for usuario in biblioteca.usuarios.values():
    print(usuario)
