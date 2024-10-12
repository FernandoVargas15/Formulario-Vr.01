import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector

def insertar_en_bd(nombres, apellidos, edad, estatura, telefono, genero):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            database="ProgAvanLFVO",
            user="root",
            password="Rocket2014"
        )
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO registros (Nombre, Apellidos, Edad, Estatura, Telefono, Genero)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (nombres, apellidos, edad, estatura, telefono, genero))
        connection.commit()

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error al insertar en la base de datos: {error}")

def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def borrar():
    limpiar_campos()

def es_entero_valido(valor):
    return valor.isdigit()

def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_telefono_valido(valor):
    return valor.isdigit() and len(valor) == 10

def es_texto_valido(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))

def guardar_valores():
    nombre = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    if not es_texto_valido(nombre):
        messagebox.showerror("Error", "Por favor, ingrese un nombre válido.")
        return
    if not es_texto_valido(apellidos):
        messagebox.showerror("Error", "Por favor, ingrese apellidos válidos.")
        return
    if not es_entero_valido(edad):
        messagebox.showerror("Error", "Por favor, ingrese una edad válida.")
        return
    if not es_decimal_valido(estatura):
        messagebox.showerror("Error", "Por favor, ingrese una estatura válida.")
        return
    if not es_telefono_valido(telefono):
        messagebox.showerror("Error", "Por favor, ingrese un teléfono de 10 dígitos.")
        return

    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"

    insertar_en_bd(nombre, apellidos, edad, estatura, telefono, genero)

    messagebox.showinfo("Éxito", "Los datos se guardaron correctamente en la base de datos.")
    limpiar_campos()

ventana = tk.Tk()
ventana.geometry("720x500")
ventana.title("Formulario Vr.01")

var_genero = tk.IntVar()

# Interfaz
lbNombre = tk.Label(ventana, text="Nombre: ")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos: ")
lbApellidos.pack()
tbApellidos = tk.Entry(ventana)
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Teléfono: ")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad: ")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="\nGénero: ")
lbGenero.pack()
rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()
btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar)
btnBorrar.pack()

ventana.mainloop()
