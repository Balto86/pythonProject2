import os

# Definimos la clase Producto
class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre}, (ID: {self.id}, Precio: {self.precio}, Cantidad: {self.cantidad})"

    def to_line(self):
        """Convertir el producto a una línea de texto para almacenamiento en archivo."""
        return f"{self.id},{self.nombre},{self.precio},{self.cantidad}\n"

    @classmethod
    def from_line(cls, line):
        """Crear un producto a partir de una línea de texto."""
        id, nombre, precio, cantidad = line.strip().split(',')
        return cls(int(id), nombre, float(precio), int(cantidad))

# Clase Inventario para gestionar múltiples productos
class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Cargar el inventario desde un archivo de texto."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    for line in file:
                        producto = Producto.from_line(line)
                        self.productos[producto.id] = producto
            except FileNotFoundError:
                print("Archivo no encontrado. Se creará un nuevo archivo.")
            except PermissionError:
                print("Error: No se tienen permisos para leer el archivo.")
            except Exception as e:
                print(f"Error inesperado al cargar el inventario: {e}")
        else:
            print("No se encontró el archivo de inventario. Se creará uno nuevo.")

    def guardar_inventario(self):
        """Guardar el inventario en un archivo de texto."""
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(producto.to_line())
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        """Agregar un producto al inventario y guardarlo en el archivo."""
        if producto.id in self.productos:
            print(f"Producto ID {producto.id} ya existe. Actualizando cantidad.")
            self.productos[producto.id].cantidad += producto.cantidad
        else:
            self.productos[producto.id] = producto
            print(f"Producto ID {producto.id} agregado al inventario.")
        self.guardar_inventario()

    def eliminar_producto(self, id):
        """Eliminar un producto del inventario y actualizar el archivo."""
        if id in self.productos:
            del self.productos[id]
            print(f"Producto ID {id} eliminado del inventario.")
            self.guardar_inventario()
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad, precio):
        """Actualizar un producto existente y guardar los cambios en el archivo."""
        if id in self.productos:
            self.productos[id].cantidad = cantidad
            self.productos[id].precio = precio
            print(f"Producto ID {id} actualizado: Cantidad = {cantidad}, Precio = {precio}.")
            self.guardar_inventario()
        else:
            print("Error: Producto no encontrado.")

    def mostrar_productos(self):
        """Mostrar todos los productos del inventario."""
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("Listado de productos en el inventario:")
            for producto in self.productos.values():
                print(producto)

# Función para mostrar el menú y manejar las opciones del usuario
def menu():
    inventario = Inventario()

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar un nuevo producto")
        print("2. Eliminar un producto")
        print("3. Actualizar un producto")
        print("4. Mostrar todos los productos")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            producto = Producto(id, nombre, precio, cantidad)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            precio = float(input("Ingrese el nuevo precio del producto: "))
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            inventario.mostrar_productos()

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
