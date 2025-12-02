from tkinter import *
from tkinter import messagebox

class View:
    def __init__(self,ventana):
        self.menu_principal(ventana)

    def borrar_pantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()


    def menu_principal(self,ventana):
        self.borrar_pantalla(ventana)
        txt_titulo = Label(ventana, text=".::Sistema de Coches::.",justify=CENTER)
        txt_titulo.pack(pady=10)
        btn_coches = Button(ventana, text="Autos",justify=CENTER, command=lambda:"")
        btn_coches.pack(pady=10)
        btn_camiones = Button(ventana,text="camiones",justify=CENTER, command=lambda:"")
        btn_camiones.pack(pady=10)
        btn_camionetas = Button(ventana,text="camionetas",justify=CENTER, command=lambda:"")
        btn_camionetas.pack(pady=10)
        btn_salir = Button(ventana,text="Salir",justify=CENTER, command=lambda:ventana.destroy())
        btn_salir.pack(pady=10)


    def menu_acciones(self,ventana):
        self.borrar_pantalla(ventana)
        txt_titulo = Label(ventana, text=".::Acciones::.",justify=CENTER)
        txt_titulo.pack(pady=10)
        btn_agregar = Button(ventana, text="Agregar",justify=CENTER, command=lambda:"")
        btn_agregar.pack(pady=10)
        btn_consultar = Button(ventana,text="Consultar",justify=CENTER, command=lambda:"")
        btn_consultar.pack(pady=10)
        btn_editar = Button(ventana,text="Editar",justify=CENTER, command=lambda:"")
        btn_editar.pack(pady=10)
        btn_borrar = Button(ventana,text="Borrar",justify=CENTER, command=lambda:"")
        btn_borrar.pack(pady=10)
        btn_volver = Button(ventana,text="Volver",justify=CENTER, command=lambda:self.menu_principal(ventana))
        btn_volver.pack(pady=10)

    def agregar_auto(self,ventana):
        self.borrar_pantalla(ventana)
        txt_titulo = Label(ventana, text=".::Agregar Auto::.",justify=CENTER)
        txt_titulo.pack(pady=10)
        lbl_marca = Label(ventana,text="Marca:",justify=CENTER)
        lbl_marca.pack(pady=5)
        entry_marca = Entry(ventana,justify=CENTER)
        entry_marca.pack(pady=5)
        lbl_color = Label(ventana,text="Color:",justify=CENTER)
        lbl_color.pack(pady=5)
        entry_color = Entry(ventana,justify=CENTER)
        entry_color.pack(pady=5)
        lbl_modelo = Label(ventana,text="Modelo:",justify=CENTER)
        lbl_modelo.pack(pady=5)
        entry_modelo = Entry(ventana,justify=CENTER)
        entry_modelo.pack(pady=5)
        lbl_velocidad = Label(ventana,text="Velocidad:",justify=CENTER)
        lbl_velocidad.pack(pady=5)
        entry_velocidad = Entry(ventana,justify=CENTER)
        entry_velocidad.pack(pady=5)
        lbl_caballaje = Label(ventana,text="Caballaje:",justify=CENTER)
        lbl_caballaje.pack(pady=5)
        entry_caballaje = Entry(ventana,justify=CENTER)
        entry_caballaje.pack(pady=5)
        lbl_plazas = Label(ventana,text="Plazas:",justify=CENTER)
        lbl_plazas.pack(pady=5)
        entry_plazas = Entry(ventana,justify=CENTER)
        entry_plazas.pack(pady=5)
        btn_guardar = Button(ventana,text="Guardar",justify=CENTER, command=lambda:"")
        btn_guardar.pack(pady=10)
        btn_volver = Button(ventana,text="Volver",justify=CENTER, command=lambda:self.menu_acciones(ventana))
        btn_volver.pack(pady=10)
    @staticmethod
    def consultar_autos(ventana,id):
        View.borrar_pantalla(ventana)
        label_titulo=Label(ventana, text=f".::Cosultar autos::.") 
        label_titulo.pack(pady=5)
        label_titulo.pack(pady=10)

        filas=""
        registros=""
        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas+=f"ID:{fila[0]} - Marca:{fila[1]} - Color:{fila[2]} - Modelo:{fila[3]} - Velocidad:{fila[4]} - Caballaje:{fila[5]} - Plazas:{fila[6]}\n"
                num_notas+=1
        else:
            messagebox.showinfo(icon="info",message="No hay autos registradas en el sistema")

        lbl_resultado=Label(ventana, text=f"{filas}")
        lbl_resultado.pack(pady=5)
        btn_volver=Button(ventana, text="Volver", command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def cambiar_auto(ventana,id,marca,color,modelo,velocidad,caballaje,plazas):
         View.borrar_pantalla(ventana)
         label1=Label(ventana, text=f".::{marca},{modelo}, Vamos a modificar un auto!!::.",justify=CENTER) 
         label1.pack(pady=10)
         lbl_id=Label(ventana, text="Ingresa el ID del auto a modificar:",justify=CENTER)
         lbl_id.pack(pady=10)
         txt_id=Entry(ventana, width=30, justify=CENTER)
         txt_id.pack(pady=10)
         lbl_marca=Label(ventana, text="Ingresa la nueva marca:",justify=CENTER)
         lbl_marca.pack(pady=10)
         entrada_marca=Entry(ventana, width=30, justify=CENTER)
         entrada_marca.pack(pady=10)
         lbl_color=Label(ventana, text="Ingresa el nuevo color:",justify=CENTER)
         lbl_color.pack(pady=10)
         entrada_color=Entry(ventana, width=30, justify=CENTER)
         entrada_color.pack(pady=10)
         lbl_modelo=Label(ventana, text="Ingresa el nuevo modelo:",justify=CENTER)
         lbl_modelo.pack(pady=10)
         entrada_modelo=Entry(ventana, width=30, justify=CENTER)
         entrada_modelo.pack(pady=10)
         lbl_velocidad=Label(ventana, text="Ingresa la nueva velocidad:",justify=CENTER)
         lbl_velocidad.pack(pady=10)
         entrada_velocidad=Entry(ventana, width=30, justify=CENTER)
         entrada_velocidad.pack(pady=10)
         lbl_caballaje=Label(ventana, text="Ingresa el nuevo caballaje:",justify=CENTER)
         lbl_caballaje.pack(pady=10)
         entrada_caballaje=Entry(ventana, width=30, justify=CENTER)
         entrada_caballaje.pack(pady=10)
         lbl_plazas=Label(ventana, text="Ingresa las nuevas plazas:",justify=CENTER)
         lbl_plazas.pack(pady=10)
         entrada_plazas=Entry(ventana, width=30, justify=CENTER)
         entrada_plazas.pack(pady=10)
         btn_guardar=Button(ventana, text="Guardar Volver", justify=CENTER,command=lambda:"")
         btn_guardar.pack(pady=10)
         btn_volver=Button(ventana, text="Volver", justify=CENTER, command=lambda: View.menu_principal(ventana))
         btn_volver.pack(pady=10)


    def borrar_auto(self,ventana):
        self.borrar_pantalla(ventana)
        txt_titulo = Label(ventana, text=".::Borrar Auto::.",justify=CENTER)
        txt_titulo.pack(pady=10)
        lbl_id = Label(ventana,text="ID del Auto a borrar:",justify=CENTER)
        lbl_id.pack(pady=5)
        entry_id = Entry(ventana,justify=CENTER)
        entry_id.pack(pady=5)
        btn_borrar = Button(ventana,text="Borrar",justify=CENTER, command=lambda:"")
        btn_borrar.pack(pady=10)
        btn_volver = Button(ventana,text="Volver",justify=CENTER, command=lambda:self.menu_acciones(ventana))
        btn_volver.pack(pady=10)

