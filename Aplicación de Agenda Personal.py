import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class EventManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Eventos")

        # Crear contenedores
        self.frame_list = tk.Frame(self.root)
        self.frame_list.pack(pady=10)

        self.frame_input = tk.Frame(self.root)
        self.frame_input.pack(pady=10)

        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(pady=10)

        # Crear TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.frame_list, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Crear campos de entrada
        self.label_date = tk.Label(self.frame_input, text="Fecha (DD/MM/AAAA):")
        self.label_date.grid(row=0, column=0)

        self.date_entry = tk.Entry(self.frame_input)
        self.date_entry.grid(row=0, column=1)

        self.label_time = tk.Label(self.frame_input, text="Hora (HH:MM):")
        self.label_time.grid(row=1, column=0)

        self.time_entry = tk.Entry(self.frame_input)
        self.time_entry.grid(row=1, column=1)

        self.label_desc = tk.Label(self.frame_input, text="Descripción:")
        self.label_desc.grid(row=2, column=0)

        self.desc_entry = tk.Entry(self.frame_input)
        self.desc_entry.grid(row=2, column=1)

        # Crear botones
        self.button_add = tk.Button(self.frame_buttons, text="Agregar Evento", command=self.add_event)
        self.button_add.grid(row=0, column=0, padx=10)

        self.button_delete = tk.Button(self.frame_buttons, text="Eliminar Evento Seleccionado",
                                       command=self.delete_event)
        self.button_delete.grid(row=0, column=1, padx=10)

        self.button_exit = tk.Button(self.frame_buttons, text="Salir", command=self.root.quit)
        self.button_exit.grid(row=0, column=2, padx=10)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        if date and time and desc:
            self.tree.insert("", "end", values=(date, time, desc))
            self.clear_entries()
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar el evento seleccionado?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = EventManager(root)
    root.mainloop()

