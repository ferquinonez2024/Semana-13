import tkinter as tk
from tkinter import messagebox

def agregar_dato():
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

def limpiar_datos():
    entrada_texto.delete(0, tk.END)
    lista_datos.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Datos")
ventana.geometry("300x250")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=10)

# Campo de texto
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=40, height=8)
lista_datos.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()

