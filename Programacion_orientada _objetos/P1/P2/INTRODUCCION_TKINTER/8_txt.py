from tkinter import *

def comentar():
    comentario=txt_comentario.get("1.0",END).strip()
    lbl_resultado.config(text=f"{comentario}")

ventana=Tk()
ventana.title("Distribución de widgers en pantalla")
gemetry="600x400"

#Opción 3: place()
lbl_comentario=Label(ventana,text="escriba su comentario:").pack()
txt_comentario=Text(ventana,width=40,height=5).pack()
boton_mostrar=Button(ventana,text="Mostrar comentario", command=comentar)
boton_mostrar.pack()
lbl_resultado=Label(ventana,text="")  
lbl_resultado.pack()  


vemtana=mainloop()