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
    def actualizar_auto(txt_id_widget, id, marca, color, modelo, velocidad, caballaje, plazas):

        auto = coches.Autos.buscar(id)

        if not auto:
            messagebox.showwarning("ID no encontrado", f"No existe el auto con ID: {id}")
            return  # no continua
        txt_id_widget.config(state="readonly")
        resultado = coches.Autos.actualizar(id, marca, color, modelo, velocidad, caballaje, plazas)

        if resultado:
            messagebox.showinfo(icon="info",title="Actualización exitosa",message=f"Auto con modelo {modelo} ha sido actualizado correctamente") 
        else:
            messagebox.showerror(icon="error",title="Error de actualización",message="No se pudo actualizar el auto")

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
