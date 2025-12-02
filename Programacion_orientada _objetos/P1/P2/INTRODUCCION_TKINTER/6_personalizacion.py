from tkinter import *
ventana=Tk()

ventana.title("Personalizar widgrts u objetos")
ventana.geometry("500x500")

etiqueta=Label(ventana,text="Bienvenidos a Tkinter")
etiqueta.config(
    bg="lightblue",
    fg="darkblue",
    width=50,
    height=5,
    font=("Helvetica",38,"italic"),
    relief="solid",
    border=2


)
etiqueta.pack(pady=25)

boton=Button(ventana,text="Haz click....")
boton.config(
    #bg="blue",
    fg="white",
    width=15,
    font=("Arial",20,"bold"),
    relief="groove",
    border=2
    activeforeground="yellow")
    #activebackground="red)

boton.pack(pady=20)
ventana.mainloop()





