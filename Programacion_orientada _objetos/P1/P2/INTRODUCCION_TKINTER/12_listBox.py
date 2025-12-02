from tkinter import *
ventana=Tk()

ventana.title("radiobutton")
ventana.geometry("500x400")
def mostrar_estado():
    seleccion=lista.get(lista.curselection())
    resultado.config(text= f"Selccionaste:{seleccion} " )

lista=Listbox(ventana,width=10, height=5, selectmode=SINGLE)
lista.pack()
opciones=["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4", "Opcion 5"]
for i in opciones:
    lista.insert(END, i)
boton=Button(ventana, text="Mostrar sleccion del usiario", command=mostrar_estado)
boton.pack()
resultado=Label(ventana, text="")
resultado.pack()



ventana.mainloop()