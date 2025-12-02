from tkinter import *
ventana=Tk()

ventana.title("checkButton")
ventana.geometry("400x400")
def mostartEstado():
    if opccion.get()==1:
        resultado.config(text="Notificaciones activadas...")
    else:
        resultado.config(text="Notificaciones Desactivadas...")

opccion=IntVar()
chequeo=Checkbutton(ventana, text="¿Desea recibir notificaciones?",variable=opccion, onvalue=1, offvalue=0)
chequeo.pack()

boton=Button(ventana, text="Confirmar", command=mostartEstado)
boton.pack()

resultado=Label(ventana, text="")
resultado.pack()
ventana.mainloop()
