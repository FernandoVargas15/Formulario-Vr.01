import tkinter as tk
from tkinter import messagebox 

#definicion de funciones
def limpiar_campos():
    tbNombre.delete(0,tk.END)
    tbApellidos.delete(0,tk.END)
    tbEdad.delete(0,tk.END)
    tbEstatura.delete(0,tk.END)
    tbTelefono.delete(0,tk.END)
    var_genero.set(0)

def borrar():
    limpiar_campos()

def guardar_valores():
    #obtener valores des de los entrys
    nombre= tbNombre.get()
    apellidos= tbApellidos.get()
    edad= tbEdad.get()
    estatura= tbEstatura.get()
    telefono= tbTelefono.get()

    #Obtener el genero de los Radiobutton
    genero = ""
    if var_genero.get()==1:
        genero= "Hombre"
    elif var_genero.get()==2:
        genero= "Mujer"

    #Generar la cadena de caracteres
    datos= "Nombres: "+ nombre + "\n"+ "Apellidos: "+ apellidos +"\n"+"Edad: "+ edad +" años\n"+"Estatura: "+ estatura +" cm\n"+"Telefono: "+ telefono +"\n"+"Genero: "+genero+"\n"

    #guardar los datos
    with open(r"C:\Users\fergu\OneDrive\Escritorio\GUARDAR_DATOS\datos2.txt", "a") as archivo:
        archivo.write(datos + "\n\n")
        messagebox.showinfo("Éxito", "Los datos se guardaron correctamente")

    #mostrar mensaje de confirmacion
    tbNombre.delete(0,tk.END)
    tbApellidos.delete(0,tk.END)
    tbEdad.delete(0,tk.END)
    tbEstatura.delete(0,tk.END)
    tbTelefono.delete(0,tk.END)
    var_genero.set(0)

ventana = tk.Tk()
ventana.geometry("720x500")
ventana.title("Formulario Vr.01")

#variable Radiobutton
var_genero = tk.IntVar()

lbNombre = tk.Label(ventana, text="Nombre: ")
lbNombre.pack()
tbNombre = tk.Entry(ventana)  # Empaquetar tbNombre
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos: ")
lbApellidos.pack()
tbApellidos = tk.Entry(ventana)  # Empaquetar tbApellidos
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Telefono: ")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)  # Empaquetar tbTelefono
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad: ")
lbEdad.pack()
tbEdad = tk.Entry(ventana)  # Empaquetar tbEdad
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)  # Empaquetar tbEstatura
tbEstatura.pack()


lbGenero=tk.Label(ventana, text="\n""Genero: ")
lbGenero.pack()
rbHombre=tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()

rbMujer=tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

#creacion de los botones
btnGuardar = tk.Button(ventana, text = "Guardar", command=guardar_valores)
btnGuardar.pack()
btnBorrar = tk.Button(ventana, text = "Borrar valores", command=borrar)
btnBorrar.pack()

#Ejecucion
ventana.mainloop()

