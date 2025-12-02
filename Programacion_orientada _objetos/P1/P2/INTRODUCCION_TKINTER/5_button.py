from tkinter import *
ventana=Tk()

ventana.title("Personalizar widgrts u objetos")
ventana.geometry("500x500")
etiqueta=Label(ventana,text="ingresa tu nombre")
etiqueta.pack()

caja=Entry(ventana)
caja.pack()


boton=Button(ventana,text="Saludar",command="")
boton.pack()

def saludar():
    caja=get()
    


ventana.mainloop()

marco=Frame(ventana)
marco.config(
    width=400,
    height=300,
    bg="lightgray",
    
)
s