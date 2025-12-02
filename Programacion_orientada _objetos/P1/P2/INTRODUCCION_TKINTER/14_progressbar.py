from tkinter import *
from tkinter import ttk
ventana=Tk()

ventana.title("radiobutton")
ventana.geometry("500x400")
def profreso():
    barrita['value']=0
    ventana.update()
    for i in range(101):
        barrita['value']=i
        ventana.update()
        ventana.after(50)
 

barrita=ttk.Progressbar(ventana,mode="indeterminate", length=200)
barrita.pack() 

boton1=Button(ventana, text="Iniciar progreso", command=profreso)
boton1.pack()
ventana.mainloop()