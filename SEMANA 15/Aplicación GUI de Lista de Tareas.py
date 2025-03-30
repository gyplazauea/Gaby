import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Vacía", "No puedes añadir una tarea vacía.")

def mark_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        task_listbox.delete(selected_index)
        task_listbox.insert(selected_index, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Selección Inválida", "Selecciona una tarea para marcarla como completada.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Selección Inválida", "Selecciona una tarea para eliminar.")

def add_task_enter(event):
    add_task()

# Configurar ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Entrada de texto
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task_enter)

# Botones
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Añadir Tarea", command=add_task).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Marcar como Completada", command=mark_completed).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Eliminar Tarea", command=delete_task).pack(side=tk.LEFT, padx=5)

# Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
