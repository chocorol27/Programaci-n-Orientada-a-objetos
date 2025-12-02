from tkinter import messagebox
from model import usuario
from view import vista
from model import nota

class Controlador:
    

    @staticmethod
    def registrar(nombre,apellidos,email,password):
        registro=usuario.Usuario.registrar(nombre,apellidos,email,password)
        if registro:
            messagebox.showinfo(icon="info", title="Registro exitoso", message="Usuario registrado correctamente")
        else:
            messagebox.showerror(icon="error", title="Error de registro", message="No se pudo registrar el usuario")
    
    @staticmethod
    def login(email, password, ventana):
        registro = usuario.Usuario.iniciar_sesion(email, password)
        if registro:
            messagebox.showinfo(icon="info", title="Login exitoso",
                                message=f"{registro[1]} {registro[2]} ha iniciado sesión correctamente")
            vista.View.menu_notas(ventana, registro[0], registro[1], registro[2])
        else:
            messagebox.showerror(icon="error", title="Error de login",
                                message="Credenciales incorrectas")
            

    @staticmethod
    def mostar_nota(usuario_id):
        registros=nota.Nota.mostrar(usuario_id)
        return registros
    
    @staticmethod
    def modificar_nota(id,titulo, descripcion):
        resultado=nota.Nota.actualizar(id,titulo,descripcion)
        if resultado:
            messagebox.showinfo(icon="info", title="Modificación exitosa", message="La nota ha sido modificada correctamente")
        else:
            messagebox.showerror(icon="error", title="Error de modificación", message="No se pudo modificar la nota")
        return resultado
    
    @staticmethod
    def crear_nota(usuario_id, titulo, descripcion, ventana):
        resultado = nota.Nota.crear(usuario_id, titulo, descripcion)
        if resultado:
            messagebox.showinfo("Creación exitosa", "La nota ha sido creada correctamente")
            # REGRESAR A MENU
            vista.View.menu_notas(ventana, usuario_id, "", "")
        else:
            messagebox.showerror("Error", "No se pudo crear la nota")


    @staticmethod
    def eliminar_nota(id):
        resultado=nota.Nota.eliminar(id)
        if resultado:
            messagebox.showinfo(icon="info", title="Eliminación exitosa", message="La nota ha sido eliminada correctamente")
        else:
            messagebox.showerror(icon="error", title="Error de eliminación", message="No se pudo eliminar la nota")




