from tkinter import *
ventana=Tk()
ventana.geometry("800x600")
ventana.title("Marcos o frame en Tkinter")
ventana.resizable(False,False)#Hace que no pueda modificcarse el tamaño de la ventana

marco1=Frame(ventana,width=400,height=200,bg="red",relief=SOLID,border=2)
marco1.pack() #Es importante para que se dibuje o muestre el objeto dentro de la ventana
marco1.pack_propagate(False)#Evitar que se modifique el estilo del marco

marco2=Frame(marco1,width=200,height=100,bg="blue",relief=GROOVE,border=10)



ventana=mainloop()