from tkinter import *
ventana=Tk()

ventana.title("radiobutton")
ventana.geometry("500x400")

def mostrar_estado():
    resultado.config(text= f"Valor seleccionado:{valor.get()} " )

valor=IntVar()
escala=Scale(ventana, from_=0, to=100, orient=HORIZONTAL, length=300, tickinterval=10, resolution=5, variable=valor, command=lambda x: mostrar_estado())
escala.pack()

boton=Button(ventana, text="Mostrar valor", command=mostrar_estado)
boton.pack()
resultado=Label(ventana, text="")
resultado.pack()


ventana.mainloop()


