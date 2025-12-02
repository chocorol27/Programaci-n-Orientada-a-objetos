from tkinter import *
import os
ventana=Tk()
ventana.title("imagenes")
ventana.geometry("500x400")
def mensaje(tipo):
    resultado.config(text= f"{tipo} " )

# Obtener la ruta absoluta del directorio donde está este archivo .py
ruta_base = os.path.dirname(os.path.abspath(__file__))
print(ruta_base)

# Construir la ruta completa al archivo de imagen
ruta_imagen = os.path.join(ruta_base, "image\logo.png")
print(ruta_imagen)

#Primer forma de agregar imagenes con la libreria de tkinter ya incluidas
#PhotoImage solo permine archivos con extension .png,.gif,.pgm,.ppm

imagen=PhotoImage(file="C:\Users\Angel\OneDrive\Escritorio\Programacion_orientada _objetos\P2\INTRODUCCION_TKINTER\logo.png")
#Incluir o mostar la imagen dentro de un label  y button
etiqueta_imagen=Label(ventana, image=imagen,compound=TOP)
etiqueta_imagen.pack()

boton=Button(ventana, image=imagen, command=lambda: mensaje("Hola python"))
boton.pack()
resultado=Label(ventana, text="")
resultado.pack()
ventana.mainloop()