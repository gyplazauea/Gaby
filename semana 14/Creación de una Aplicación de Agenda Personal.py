import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Frame de entrada
        frame_input = tk.Frame(root)
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Fecha:").grid(row=0, column=0)
        self.date_entry = DateEntry(frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame_input, text="Hora:").grid(row=1, column=0)
        self.time_entry = tk.Entry(frame_input, width=10)
        self.time_entry.grid(row=1, column=1, padx=5)

        tk.Label(frame_input, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(frame_input, width=30)
        self.desc_entry.grid(row=2, column=1, padx=5)

        tk.Button(frame_input, text="Agregar Evento", command=self.agregar_evento).grid(row=3, columnspan=2, pady=5)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=10)

        # Botón para eliminar eventos
        tk.Button(root, text="Eliminar Evento", command=self.eliminar_evento).pack(pady=5)
        tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

    def agregar_evento(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar completos")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Deseas eliminar este evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
