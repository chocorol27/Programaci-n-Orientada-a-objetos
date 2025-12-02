from tkinter import *
ventana=Tk()

ventana.title("radiobutton")
ventana.geometry("500x400")
from tkinter import *
ventana=Tk()

ventana.title("checkButton")
ventana.geometry("400x400")
def mostartEstado():
    if opcion.get()==1:
        resultado.config(text="opccion 1...")
    elif opcion.get()==2:
        resultado.config(text="Opccion 2...")
    elif opcion.get()==3:
        resultado.config(text="Opccion3...")
opcion=StringVar()
radioboton=Radiobutton(ventana, text="Opcion 1",variable=opcion, value="Opcion 1")
radioboton.pack()

radioboton2=Radiobutton(ventana, text="Opcion 2",variable=opcion, value="Opcion 2")
radioboton2.pack()

radioboton3=Radiobutton(ventana, text="Opcion 3",variable=opcion, value="Opcion 3")
radioboton3.pack()

boton=Button(ventana, text="Mostart seleccion", command=mostartEstado)
boton.pack()

resultado=Label(ventana, text="")
resultado.pack()
ventana.mainloop()

