import tkinter as tk
from tkinter import messagebox
import csv

ENTRADAS_FILE = "entradas.csv" 

def cargar_entradas(email):
    entradas = []
    try:
        with open(ENTRADAS_FILE, newline='') as file:
            lector = csv.reader(file)
            for fila in lector:
                if fila[0] == email:
                    entradas.append(f"{fila[1]} - {fila[2]}")
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de entradas no encontrado.")
    return entradas

def iniciar_sesion():
    email = email_entry.get().strip()
    if not email:
        messagebox.showwarning("Aviso", "Por favor, ingresa tu correo.")
        return

    entradas = cargar_entradas(email)
    if entradas:
        mostrar_entradas(email, entradas)
    else:
        messagebox.showinfo("Sin entradas", "No se encontraron entradas para este correo.")

def mostrar_entradas(email, entradas):
    ventana = tk.Toplevel(root)
    ventana.title(f"Entradas de {email}")
    tk.Label(ventana, text=f"Entradas para {email}", font=("Arial", 14)).pack(pady=10)
    
    for entrada in entradas:
        tk.Label(ventana, text=entrada).pack(anchor='w', padx=20)

root = tk.Tk()
root.title("Inicio de Sesión - Comprador")

tk.Label(root, text="Ingresa tu correo:", font=("Arial", 12)).pack(pady=10)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

tk.Button(root, text="Iniciar sesión", command=iniciar_sesion).pack(pady=10)

root.mainloop()
