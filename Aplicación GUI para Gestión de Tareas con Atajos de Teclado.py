import tkinter as tk
from tkinter import messagebox, Listbox, END, SINGLE

class TaskManager:
    def __init__(self, root):
        # Inicializa la ventana principal de la aplicación
        self.root = root
        self.root.title("Gestión de Tareas")

        # Lista para almacenar las tareas
        self.tasks = []

        # Campo de entrada para añadir nuevas tareas
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)  # Añade un margen vertical

        # Botón para añadir una nueva tarea
        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Botón para marcar una tarea como completada
        self.complete_task_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Botón para eliminar una tarea
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Lista que muestra las tareas
        self.task_listbox = Listbox(root, selectmode=SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Asignación de atajos de teclado
        self.root.bind('<Return>', self.add_task_shortcut)  # Añadir tarea con "Enter"
        self.root.bind('<c>', self.complete_task_shortcut)  # Marcar como completada con "C"
        self.root.bind('<Delete>', self.delete_task_shortcut)  # Eliminar tarea con "Delete"
        self.root.bind('<Escape>', self.close_app)  # Cerrar aplicación con "Escape"

    def add_task(self, event=None):
        # Método para añadir una nueva tarea
        task = self.task_entry.get()  # Obtiene el texto del campo de entrada
        if task:  # Verifica si el campo no está vacío
            self.tasks.append(task)  # Añade la tarea a la lista
            self.update_task_list()  # Actualiza la visualización de tareas
            self.task_entry.delete(0, END)  # Limpia el campo de entrada
        else:
            # Muestra un mensaje de advertencia si el campo está vacío
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def complete_task(self, event=None):
        # Método para marcar una tarea como completada
        selected_task_index = self.task_listbox.curselection()  # Obtiene el índice de la tarea seleccionada
        if selected_task_index:  # Verifica si hay una tarea seleccionada
            # Marca la tarea como completada añadiendo texto
            completed_task = self.tasks[selected_task_index[0]] + " (Completada)"
            self.tasks[selected_task_index[0]] = completed_task  # Actualiza la tarea en la lista
            self.update_task_list()  # Actualiza la visualización de tareas
        else:
            # Muestra un mensaje de advertencia si no hay tarea seleccionada
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea.")

    def delete_task(self, event=None):
        # Método para eliminar una tarea
        selected_task_index = self.task_listbox.curselection()  # Obtiene el índice de la tarea seleccionada
        if selected_task_index:  # Verifica si hay una tarea seleccionada
            del self.tasks[selected_task_index[0]]  # Elimina la tarea de la lista
            self.update_task_list()  # Actualiza la visualización de tareas
        else:
            # Muestra un mensaje de advertencia si no hay tarea seleccionada
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea.")

    def update_task_list(self):
        # Método para actualizar la lista de tareas en la interfaz
        self.task_listbox.delete(0, END)  # Limpia la lista visual
        for task in self.tasks:  # Recorre la lista de tareas
            self.task_listbox.insert(END, task)  # Inserta cada tarea en la lista visual

    def add_task_shortcut(self, event):
        # Atajo para añadir una tarea usando la tecla "Enter"
        self.add_task()

    def complete_task_shortcut(self, event):
        # Atajo para marcar una tarea como completada usando la tecla "C"
        self.complete_task()

    def delete_task_shortcut(self, event):
        # Atajo para eliminar una tarea usando la tecla "Delete"
        self.delete_task()

    def close_app(self, event):
        # Método para cerrar la aplicación
        self.root.quit()

# Punto de entrada para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = TaskManager(root)  # Inicializa la aplicación
    root.mainloop()  # Inicia el bucle principal de la aplicación
