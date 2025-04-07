import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Entrada de tarea
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.focus()

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE, width=40, height=15)
        self.task_listbox.pack()

        # Botones
        frame = tk.Frame(root)
        frame.pack(pady=10)

        self.add_button = tk.Button(frame, text="Añadir", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(frame, text="Completar", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(frame, text="Eliminar", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Enlace de atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<C>', lambda event: self.complete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<D>', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese una tarea.")

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task_text = self.task_listbox.get(index)
            if not task_text.startswith("✔"):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"✔ {task_text}")
        else:
            messagebox.showinfo("Sin selección", "Seleccione una tarea para marcar como completada.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected[0])
        else:
            messagebox.showinfo("Sin selección", "Seleccione una tarea para eliminar.")

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
