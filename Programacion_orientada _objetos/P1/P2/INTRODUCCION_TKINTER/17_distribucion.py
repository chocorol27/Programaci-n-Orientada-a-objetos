from tkinter import *
ventana=Tk()
ventana.title("Distribución de widgers en pantalla")
#Opccion 1: pack() con side=left o side=right
Label(ventana,text="Nombre").pack(anchor="nw",side=TOP,padx=5,pady=5)
Entry(ventana).pack(anchor="nw",side=TOP,padx=5,pady=5)
Label(ventana,text="contraseña").pack(anchor="nw",side=TOP,padx=50,pady=5)
Entry(ventana).pack(anchor="nw",side=TOP,padx=50,pady=5)


#opccion 2 grid()
Label(ventana,text="Nombre").grid(row=0,column=0,padx=5,pady=5)
Entry(ventana).grid(row=0,column=1,padx=5,pady=5)
Label(ventana,text="contraseña").grid(row=1,column=0,padx=5,pady=5)
Entry(ventana).grid(row=1,column=1,padx=5,pady=5)


vemtana=mainloop()