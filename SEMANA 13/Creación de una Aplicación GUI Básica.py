import tkinter as tk
from tkinter import messagebox

def agregar_dato():
    """Agrega el dato ingresado en el campo de texto a la lista."""
    dato = entrada.get().strip()
    if dato:
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío. Por favor, ingrese un dato.")

def limpiar_lista():
    """Elimina todos los elementos de la lista."""
    if lista.size() > 0:
        lista.delete(0, tk.END)
    else:
        messagebox.showinfo("Información", "La lista ya está vacía.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Aplicación GUI - Lista de Datos")
root.geometry("400x350")
root.resizable(False, False)

# Marco principal
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=10)

# Etiqueta
label = tk.Label(frame, text="Ingrese un dato:", font=("Arial", 12))
label.pack(pady=5)

# Campo de texto
entrada = tk.Entry(frame, width=40, font=("Arial", 12))
entrada.pack(pady=5)

# Botones
btn_frame = tk.Frame(frame)
btn_frame.pack(pady=5)

btn_agregar = tk.Button(btn_frame, text="Agregar", command=agregar_dato, width=15, bg="#4CAF50", fg="white", font=("Arial", 10))
btn_agregar.grid(row=0, column=0, padx=5)

btn_limpiar = tk.Button(btn_frame, text="Limpiar", command=limpiar_lista, width=15, bg="#F44336", fg="white", font=("Arial", 10))
btn_limpiar.grid(row=0, column=1, padx=5)

# Lista para mostrar los datos
lista = tk.Listbox(frame, width=50, height=10, font=("Arial", 10))
lista.pack(pady=5)

# Iniciar la aplicación
root.mainloop()
