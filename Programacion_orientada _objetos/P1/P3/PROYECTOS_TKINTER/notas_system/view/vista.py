from tkinter import *
from tkinter import messagebox
from controller import controlador
from model import usuario

class View:
    def __init__(self,ventana):
        self.menu_principal(ventana)

    def menu_principal(self, ventana):
        self.borrar_pantalla(ventana)

        label_titulo=Label(ventana, text=".::Menu principal::.") 
        label_titulo.pack(pady=5)
        label_titulo.config()

        boton_registro=Button(ventana, text="1.-Registro",command=lambda: self.registro_usuario(ventana))
        boton_registro.pack(pady=5)
        boton_registro.config()

        boton_login=Button(ventana, text="2.-Login", command=lambda: self.login(ventana))
        boton_login.pack(pady=5)
        boton_login.config()

        boton_salir=Button(ventana, text="3.-Salir")
        boton_salir.pack(pady=5)
        boton_salir.config()
        


    def registro_usuario(self, ventana):
        self.borrar_pantalla(ventana)
        txt_1 = Label(ventana, text=".::Registro en el sistema::.",justify=CENTER)
        txt_1.pack(pady=10)
        
        txt_2 = Label(ventana, text="Ingresa tu nombre:", justify=CENTER)
        txt_2.pack(pady=10)
        
        entrada_nombre = Entry(ventana, width=30,justify=CENTER)
        entrada_nombre.pack(pady=10)
        
        txt_3 = Label(ventana, text="Ingresa tus apellidos:",justify=CENTER)
        txt_3.pack(pady=10)
        
        entrada_apellidos = Entry(ventana, width=30,justify=CENTER)
        entrada_apellidos.pack(pady=10)

        txt_4 = Label(ventana, text="Ingresa tu email:", justify=CENTER)
        txt_4.pack(pady=10)
        
        entrada_email = Entry(ventana, width=30,justify=CENTER)
        entrada_email.pack(pady=10)
        
        txt_5 = Label(ventana, text="Ingresa tu password:",justify=CENTER)
        txt_5.pack(pady=10)
        
        entrada_password = Entry(ventana, width=30, show="*",justify=CENTER)
        entrada_password.pack(pady=10)
        
        boton_registrarse = Button(ventana, text="Registrarse",justify=CENTER, command=lambda: controlador.Controlador.registrar(entrada_nombre.get(), entrada_apellidos.get(), entrada_email.get(), entrada_password.get()))
        boton_registrarse.pack(pady=10)
        
        boton_volver = Button(ventana, text="Volver",justify=CENTER, command=lambda: self.menu_principal(ventana))
        boton_volver.pack(pady=10)
        

    def login(self,ventana):
        self.borrar_pantalla(ventana)
        txt_1 = Label(ventana, text=".::Registro en el sistema::.",justify=CENTER)
        txt_1.pack(pady=10)
        
        txt_2 = Label(ventana, text="Ingresa tu email:", justify=CENTER)
        txt_2.pack(pady=10)
        
        entrada_email = Entry(ventana, width=30,justify=CENTER)
        entrada_email.pack(pady=10)
        
        txt_3 = Label(ventana, text="Ingresa tu password:",justify=CENTER)
        txt_3.pack(pady=10)
        
        entrada_password = Entry(ventana, width=30, show="*",justify=CENTER)
        entrada_password.pack(pady=10)
        boton_registrarse = Button(ventana, text="Iniciar sesión",justify=CENTER, command=lambda: controlador.Controlador.login(entrada_email.get(), entrada_password.get(), ventana))
        boton_registrarse.pack(pady=10)
        
        
        boton_registrarse = Button(ventana, text="Volver",justify=CENTER)
        boton_registrarse.pack(pady=10)
      
    @staticmethod
    def borrar_pantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_notas(ventana,id,nombre,apellido):
        View.borrar_pantalla(ventana)
        bienvenida = Label(ventana, text=f":: Bienvenido {nombre}, {apellido} has iniciado sesión ::", justify=CENTER) 
        bienvenida.pack(pady=5)

        btn1 = Button(ventana, text="1.- Crear",command=lambda: View.crear_nota(ventana, id, nombre, apellido))
        btn1.pack(pady=5)

        btn2 = Button(ventana, text="2.- Mostrar",command=lambda: View.mostrar_notas(id,nombre,apellido, ventana))
        btn2.pack(pady=5)

        btn3 = Button(ventana, text="3.- Cambiar",command=lambda: View.cambiar_nota(ventana, id, nombre, apellido))
        btn3.pack(pady=5)

        btn4 = Button(ventana, text="4.- Eliminar" ,command=lambda: View.borrar_nota(ventana, id, nombre, apellido))
        btn4.pack(pady=5)

        btn5 = Button(ventana, text="5.- Regresar")
        btn5.pack(pady=5)



       



    @staticmethod
    def mostrar_notas(usuario_id,nombre,apellido, ventana):
        View.borrar_pantalla(ventana)
        label_titulo=Label(ventana, text=f".::{nombre},{apellido}, Menu de notas::.") 
        label_titulo.pack(pady=5)
        label_titulo.pack(pady=10)

        filas=""
        registros=controlador.Controlador.mostar_nota(usuario_id)
        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas+=f"ID:{fila[0]} - Usuario_id:{fila[1]} - Titulo:{fila[2]} - Descripcion:{fila[3]} - Fecha:{fila[4]}\n"
                num_notas+=1
        else:
            messagebox.showinfo(icon="info",message="No hay notas registradas en el sistema")

        lbl_resultado=Label(ventana, text=f"{filas}")
        lbl_resultado.pack(pady=5)
        btn_volver=Button(ventana, text="Volver", command=lambda: View.menu_notas(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def cambiar_nota(ventana,id,nombre,apellido):
         View.borrar_pantalla(ventana)
         label1=Label(ventana, text=f".::{nombre},{apellido}, Vamos a modificar una nota!!::.",justify=CENTER) 
         label1.pack(pady=10)
         lbl_id=Label(ventana, text="Ingresa el ID de la nota a modificar:",justify=CENTER)
         lbl_id.pack(pady=10)
         txt_id=Entry(ventana, width=30, justify=CENTER)
         txt_id.pack(pady=10)
         lbl_titulo=Label(ventana, text="Ingresa el nuevo titulo:",justify=CENTER)
         lbl_titulo.pack(pady=10)
         entrada_titulo=Entry(ventana, width=30, justify=CENTER)
         entrada_titulo.pack(pady=10)
         lbl_descripcion=Label(ventana, text="Ingresa la nueva descripcion:",justify=CENTER)
         lbl_descripcion.pack(pady=10)
         entrada_descripcion=Entry(ventana, width=30, justify=CENTER)
         entrada_descripcion.pack(pady=10)
         btn_guardar=Button(ventana, text="Guardar Volver", justify=CENTER,command=lambda:controlador.Controlador.modificar_nota(txt_id.get(), entrada_titulo.get(), entrada_descripcion.get()))
         btn_guardar.pack(pady=10)
         btn_volver=Button(ventana, text="Volver", justify=CENTER, command=lambda: View.menu_notas(ventana,id,nombre,apellido))
         btn_volver.pack(pady=10)

    @staticmethod
    def crear_nota(ventana, usuario_id,titulo, descripcion):
        View.borrar_pantalla(ventana)

        label1 = Label(ventana, text=".::Crear una nueva nota::.", justify=CENTER)
        label1.pack(pady=10)

        lbl_titulo = Label(ventana, text="Ingresa el titulo:", justify=CENTER)
        lbl_titulo.pack(pady=10)

        entrada_titulo = Entry(ventana, width=30, justify=CENTER)
        entrada_titulo.pack(pady=10)

        lbl_descripcion = Label(ventana, text="Ingresa la descripcion:", justify=CENTER)
        lbl_descripcion.pack(pady=10)

        entrada_descripcion = Entry(ventana, width=30, justify=CENTER)
        entrada_descripcion.pack(pady=10)

        btn_guardar = Button(ventana,text="Guardar",justify=CENTER,command=lambda: controlador.Controlador.crear_nota(
            usuario_id,
            entrada_titulo.get(),
            entrada_descripcion.get(),
            ventana
        ))
        btn_guardar.pack(pady=10)

        btn_volver = Button( ventana, text="Volver",justify=CENTER, command=lambda: View.menu_notas(ventana, usuario_id, titulo, descripcion))

        btn_volver.pack(pady=10)


    @staticmethod
    def borrar_nota(ventana, id, nombre, apellido):
        View.borrar_pantalla(ventana)
        lbl_ti=Label(ventana, text=f".::{nombre},{apellido}, Vamos a eliminar una nota!!::.",justify=CENTER)
        lbl_ti.pack(pady=10)
        lbl_id=Label(ventana, text="Ingresa el ID de la nota a eliminar:",justify=CENTER)
        lbl_id.pack(pady=10)
        entrada_id=Entry(ventana, width=30, justify=CENTER)
        entrada_id.pack(pady=10)
        btn_eliminar=Button(ventana, text="Eliminar", justify=CENTER ,command=lambda:controlador.Controlador.eliminar_nota(entrada_id.get()))
        btn_eliminar.pack(pady=10)
        btn_volver=Button(ventana, text="Volver", justify=CENTER, command=lambda: View.menu_notas(ventana,id,nombre,apellido))
        btn_volver.pack(pady=10)

      
        