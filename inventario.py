# definimos la clase producto
class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre}, (ID: {self.id}, Precio: {self.precio}, Cantidad: {self.cantidad})"


# Creamos productos que se encuentran en la empresa
producto1 = Producto(id=1, nombre="helados", precio=0.25, cantidad=250)
print("Producto 1 creado:", producto1)

producto2 = Producto(id=2, nombre="chocolates", precio=1.25, cantidad=125)
print("Producto 2 creado:", producto2)

producto3 = Producto(id=3, nombre="caramelos", precio=0.15, cantidad=220)
print("Producto 3 creado:", producto3)


# Clase Inventario para gestionar múltiples productos

# Usamos un diccionario para almacenar productos por ID
class Inventario:
    def __init__(self):
        self.productos = {}

# nos ayuda a ingresar productos nuevos
    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print(f"Producto ID {producto.id} ya existe. Actualizando cantidad.")
            self.productos[producto.id].cantidad += producto.cantidad
        else:
            self.productos[producto.id] = producto
            print(f"Producto ID {producto.id} agregado al inventario.")

# nos ayuda para eliminar productos que ya no se encuentran en exitencia
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(f"Producto ID {id} eliminado del inventario.")
        else:
            print("Error: Producto no encontrado.")

# nos ayuda para ingresar los nuevos productos y sus cambios de precio y cantidad
    def actualizar_producto(self, id, cantidad, precio):
        if id in self.productos:
            self.productos[id].cantidad = cantidad
            self.productos[id].precio = precio
            print(f"Producto ID {id} actualizado: Cantidad = {cantidad}, Precio = {precio}.")
        else:
            print("Error: Producto no encontrado.")
# nos ayuda para saber la existencia de productos en el inventario
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("Listado de productos en el inventario:")
            for producto in self.productos.values():
                print(producto)


# Crear Inventario
inventario = Inventario()

# Agregar productos al inventario
print("\nAgregando productos al inventario:")
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

# Mostrar productos en el inventario
print("\nProductos en el inventario después de agregar:")
inventario.mostrar_productos()

# Actualizar un producto
print("\nActualizando producto ID 2:")
inventario.actualizar_producto(id=2, cantidad=150, precio=1.50)

# Mostrar productos después de la actualización
print("\nProductos en el inventario después de la actualización:")
inventario.mostrar_productos()

# Eliminar un producto
print("\nEliminando producto ID 1:")
inventario.eliminar_producto(id=1)

# Mostrar productos después de eliminar uno
print("\nProductos en el inventario después de eliminar uno:")
inventario.mostrar_productos()

# Función para mostrar el menú y manejar las opciones del usuario
def menu():
    inventario = Inventario()

    # Productos iniciales
    inventario.agregar_producto(Producto(id=1, nombre="helados", precio=0.25, cantidad=250))
    inventario.agregar_producto(Producto(id=2, nombre="chocolates", precio=1.25, cantidad=125))
    inventario.agregar_producto(Producto(id=3, nombre="caramelos", precio=0.15, cantidad=220))

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