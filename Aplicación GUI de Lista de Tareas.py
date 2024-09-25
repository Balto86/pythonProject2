import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Campo de entrada para nuevas tareas
        self.task_input = tk.Entry(root, width=40)
        self.task_input.pack(pady=10)

        # Botón para añadir tarea
        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Botón para marcar tarea como completada
        self.complete_task_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Listbox para mostrar tareas
        self.task_list = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_list.pack(pady=10)

        # Manejo de eventos
        self.task_input.bind("<Return>", lambda event: self.add_task())

    def add_task(self):
        """Añadir una nueva tarea a la lista."""
        task = self.task_input.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_input.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def complete_task(self):
        """Marcar la tarea seleccionada como completada."""
        try:
            selected_index = self.task_list.curselection()[0]
            task = self.task_list.get(selected_index)
            self.task_list.delete(selected_index)  # Eliminar la tarea de la lista
            self.task_list.insert(selected_index, task + " (Completada)")  # Añadir "(Completada)"
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        """Eliminar la tarea seleccionada de la lista."""
        try:
            selected_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
