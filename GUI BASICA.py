
import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_info():
    info = entry.get()  # Obtener el texto del campo de texto
    if info:
        listbox.insert(tk.END, info)  # Insertar la información en la lista
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")  # Mostrar advertencia si el campo está vacío

# Función para limpiar la información
def limpiar_info():
    entry.delete(0, tk.END)  # Limpiar el campo de texto
    listbox.delete(0, tk.END)  # Limpiar la lista

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Información")  # Establecer el título de la ventana

# Crear y colocar los componentes
label = tk.Label(root, text="Ingrese la información:")  # Etiqueta descriptiva
label.pack(pady=10)  # Colocar la etiqueta en la ventana

entry = tk.Entry(root, width=50)  # Campo de texto para la entrada del usuario
entry.pack(pady=5)  # Colocar el campo de texto en la ventana

agregar_btn = tk.Button(root, text="Agregar", command=agregar_info)  # Botón para agregar información
agregar_btn.pack(pady=5)  # Colocar el botón en la ventana

listbox = tk.Listbox(root, width=50, height=10)  # Lista para mostrar la información
listbox.pack(pady=10)  # Colocar la lista en la ventana

limpiar_btn = tk.Button(root, text="Limpiar", command=limpiar_info)  # Botón para limpiar la información
limpiar_btn.pack(pady=5)  # Colocar el botón en la ventana

# Iniciar el bucle principal de la aplicación
root.mainloop()
