from tkinter import messagebox
from model import coches
from view import vista




class Controlador:
    @staticmethod
    def insertar_auto(marca,color,modelo,velocidad,caballaje,plazas):
        registro=coches.Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas)
        if registro:
            messagebox.showinfo(icon="info", title="Inserción exitosa", message="Auto insertado correctamente")
        else:
            messagebox.showerror(icon="error", title="Error de inserción", message="No se pudo insertar el auto")



    @staticmethod
    def consultar_autos():
        registros=coches.Autos.consultar()
        return registros
    

    @staticmethod
    def buscar_auto(ventana, id, tipo):
        auto = coches.Autos.buscar(id)

        if not auto:
            messagebox.showerror("Error", f"No existe un auto con ID: {id}")
            return

        vista.View.cambiar_auto(
            ventana,
            auto[0],  
            auto[1],  
            auto[2],  
            auto[3],  
            auto[4],  
            auto[5],  
            auto[6],  
            tipo
        )
    @staticmethod
    def actualizar_auto(id,marca, color, modelo, velocidad, caballaje, plazas):
        coches.Autos.actualizar(marca, color, modelo, velocidad, caballaje, plazas, id)
        messagebox.showinfo(icon="info", title="Actualización exitosa", message=f"Auto con ID {id} ha sido actualizado correctamente")

    @staticmethod
    def eliminar_auto(txt_id_widget,id):
        resultado=coches.Autos.buscar(id)
        if not resultado:
            messagebox.showwarning("ID no encontrado", f"No existe el auto con ID: {id}")
            return
        txt_id_widget.config(state="readonly")
        registro=coches.Autos.eliminar(id)
        if registro:
            messagebox.showinfo(icon="info", title="Eliminación exitosa", message=f"Auto con ID {id} ha sido eliminado correctamente")
        else:
            messagebox.showerror(icon="error", title="Error de eliminación", message="No se pudo eliminar el auto")
    
    @staticmethod
    def insertar_camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        registro=coches.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
        if registro:
            messagebox.showinfo(icon="info", title="Inserción exitosa", message="Camioneta insertada correctamente")
        else:
            messagebox.showerror(icon="error", title="Error de inserción", message="No se pudo insertar la camioneta")
   
    @staticmethod
    def consultar_camionetas():
        registros=coches.Camionetas.consultar()
        return registros
    
    @staticmethod
    def buscar_camioneta(ventana, id, tipo):
        camioneta = coches.Camionetas.buscar(id)

        if not camioneta:
            messagebox.showerror("Error", f"No existe una camioneta con ID: {id}")
            return

        vista.View.cambiar_camionetas(
            ventana,
            camioneta[0],  
            camioneta[1],  
            camioneta[2],  
            camioneta[3],  
            camioneta[4],  
            camioneta[5],  
            camioneta[6],  
            camioneta[7],
            camioneta[8],
            tipo
        )


    @staticmethod
    def actualizar_camioneta(id,marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        coches.Camionetas.actualizar(marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada, id)
        messagebox.showinfo(icon="info", title="Actualización exitosa", message=f"Camioneta con ID {id} ha sido actualizada correctamente")

    @staticmethod
    def eliminar_camioneta(txt_id_widget,id):
        resultado=coches.Camionetas.buscar(id)
        if not resultado:
            messagebox.showwarning("ID no encontrado", f"No existe la camioneta con ID: {id}")
            return
        txt_id_widget.config(state="readonly")
        registro=coches.Camionetas.eliminar(id)
        if registro:
            messagebox.showinfo(icon="info", title="Eliminación exitosa", message=f"Camioneta con ID {id} ha sido eliminada correctamente")
        else:
            messagebox.showerror(icon="error", title="Error de eliminación", message="No se pudo eliminar la camioneta")


    @staticmethod
    def insertar_camion(marca,color,modelo,velocidad,caballaje,plazas,ejes,capacidad_carga):
        registro=coches.Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,ejes,capacidad_carga)
        if registro:
            messagebox.showinfo(icon="info", title="Inserción exitosa", message="Camión insertado correctamente")
        else:
            messagebox.showerror(icon="error", title="Error de inserción", message="No se pudo insertar el camión")


    @staticmethod
    def consultar_camiones():
        registros=coches.Camiones.consultar()
        return registros
    
    @staticmethod
    def buscar_camion(ventana, id, tipo):
        camion = coches.Camiones.buscar(id)

        if not camion:
            messagebox.showerror("Error", f"No existe un camión con ID: {id}")
            return

        vista.View.cambiar_camiones(
            ventana,
            camion[0],  
            camion[1],  
            camion[2],  
            camion[3],  
            camion[4],  
            camion[5],  
            camion[6],  
            camion[7],
            camion[8],
            tipo
        )



    @staticmethod
    def actualizar_camion(id,marca, color, modelo, velocidad, caballaje,plazas, ejes, capacidad_carga):
        coches.Camiones.actualizar(marca, color, modelo, velocidad, caballaje,plazas ,ejes, capacidad_carga, id)
        messagebox.showinfo(icon="info", title="Actualización exitosa", message=f"Camión con ID {id} ha sido actualizado correctamente")

    @staticmethod
    def eliminar_camion(txt_id_widget,id):  
        resultado=coches.Camiones.buscar(id)
        if not resultado:
            messagebox.showwarning("ID no encontrado", f"No existe el camión con ID: {id}")
            return
        txt_id_widget.config(state="readonly")
        registro=coches.Camiones.eliminar(id)
        if registro:
            messagebox.showinfo(icon="info", title="Eliminación exitosa", message=f"Camión con ID {id} ha sido eliminado correctamente")
        else:
            messagebox.showerror(icon="error", title="Error de eliminación", message="No se pudo eliminar el camión")

    
