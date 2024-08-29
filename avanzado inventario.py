#La clase Producto representará los ítems del inventario
# con los atributos necesarios y métodos para acceder y modificar estos atributos.
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

#La clase Inventario manejará la colección de productos utilizando un diccionario
# para el almacenamiento en memoria y funciones para manejar el almacenamiento en archivo
#Diccionario: Se usa para almacenar
# los productos en la clase Inventario, permitiendo acceso rápido y eficiente por ID.
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print(f"Producto con ID {producto.get_id()} ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("Producto actualizado exitosamente.")
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

#Archivos de Texto: Los datos del inventario se guardan y cargan en formato
# de texto,con cada línea representando un producto. Los campos se separan por comas.

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            for producto in self.productos.values():
                f.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
        print(f"Inventario guardado en {archivo}.")

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                self.productos = {}
                for linea in f:
                    id, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(id, nombre, int(cantidad), float(precio))
                    self.productos[id] = producto
            print(f"Inventario cargado desde {archivo}.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

#El menú interactivo en la consola permitirá
# al usuario realizar operaciones sobre el inventario.


def menu():
    print("\n--- Sistema de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("0. Salir")


def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            archivo = input("Nombre del archivo para guardar el inventario (ejemplo.txt): ")
            inventario.guardar_inventario(archivo)

        elif opcion == '7':
            archivo = input("Nombre del archivo para cargar el inventario (ejemplo.txt): ")
            inventario.cargar_inventario(archivo)

        elif opcion == '0':
            print("Saliendo...")
            break

        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    main()
