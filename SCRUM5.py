import tkinter as tk
from tkinter import messagebox
import csv

# Simula una "base de datos" de usuarios con contraseñas
USUARIOS_FILE = "usuarios.csv"  # Debe tener: email,contraseña

def recuperar_contraseña():
    email = email_entry.get().strip()
    if not email:
        messagebox.showwarning("Aviso", "Por favor, ingresa tu correo.")
        return

    try:
        with open(USUARIOS_FILE, newline='') as file:
            lector = csv.reader(file)
            for fila in lector:
                if fila[0] == email:
                    messagebox.showinfo("Contraseña encontrada", f"Tu contraseña es: {fila[1]}")
                    return
            messagebox.showerror("No encontrado", "Correo no registrado.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de usuarios no encontrado.")

# GUI
root = tk.Tk()
root.title("Recuperar contraseña")

tk.Label(root, text="Recupera tu contraseña", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="Ingresa tu correo electrónico:").pack()

email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

tk.Button(root, text="Recuperar contraseña", command=recuperar_contraseña).pack(pady=10)

root.mainloop()

