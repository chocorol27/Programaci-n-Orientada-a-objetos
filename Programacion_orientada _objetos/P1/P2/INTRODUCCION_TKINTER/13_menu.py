from tkinter import *
ventana=Tk()

ventana.title("radiobutton")
ventana.geometry("500x400")
def mostrar_estado(tipo):
    resultado.config(text= f"{tipo}" )

menubar=Menu(ventana)
ventana.config(menu=menubar)
archivoMenu=Menu(menubar, tearoff=False)
menubar.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo archivo", command=lambda:mostrar_estado("Nuevo archivo "))
archivoMenu.add_command(label=" Guardar archivo", command=lambda:mostrar_estado("Guardar archivo "))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=ventana.quit)

resultado=Label(ventana, text="")
resultado.pack()
ventana.mainloop()