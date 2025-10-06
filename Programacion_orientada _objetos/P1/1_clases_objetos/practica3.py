import os
os.system("cls")

class Profesores:
   
    
    def __init__(self,nombre,experiencia,num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor
    
    @property
    def nombre(self):
        return self.__nombre
    #setter
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def experiencia(self):
        return self.__experiencia
    #setter
    @experiencia.setter
    def marca(self,experiencia):
        self.__experiencia=experiencia

    @property
    def num_profesor(self):
        return self.__num_profesor
    #setter
    @num_profesor.setter
    def num_profesor(self,num_profesor):
        self.__num_profesor=num_profesor

    

    def impartir(self):
        print("Imparte clase")
        pass
    def evaluar(self):
        print("Evalua mi clase de programacion")
profesor1=Profesores()
profesor1.set_nombre("Juan")
profesor1.set_experiencia("10 años")
profesor1.set_num_profesor("3284128")

profesor2=Profesores()
profesor2.set_nombre("Pedro")
profesor2.set_experiencia("5 años")
profesor2.set_num_profesor("3284988")




class Alumnos:
   
    
    def __init__(self,nombre,edad,matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula
    
    @property
    def nombre(self):
        return self.__nombre
    #setter
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def edad(self):
        return self.__edad
    #setter
    @edad.setter
    def experiencia(self,edad):
        self.__edad=edad

    @property
    def matricula(self):
        return self.__matricula
    #setter
    @matricula.setter
    def num_profesor(self,matricula):
        self.__matricula=matricula

    

    def incribirse(self):
       return "Se inscribe en el nuevo cuatri"
    def estudiar(self):
        return "Estudia programacion"


alumno1=Alumnos()
alumno1.set_nombre("luis")
alumno1.set_edad("19 años")
alumno1.set_matricula("3284128")

alumno2=Alumnos()
alumno2.set_nombre("Alberto")
alumno2.set_edad("22 años")
alumno2.set_matricula("3141577888")


class Cursos: 
   
    
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos
    
    @property
    def nombre(self):
        return self.__nombre
    #setter
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def codigo(self):
        return self.__codigo
    #setter
    @codigo.setter
    def experiencia(self,codigo):
        self.__codigo=codigo

    @property
    def creditos(self):
        return self.__creditos
    #setter
    @creditos.setter
    def num_profesor(self,creditos):
        self.__creditos=creditos

    def asignar(self):
      return "Sera asignada el nuevo cuatri"

alumno1=Alumnos()
alumno1.set_nombre("luis") 
alumno1.set_edad("19 años")
profesor1.set_matricula("3284128")

alumno2=Alumnos()
alumno2.set_nombre("Alberto")
alumno2.set_edad("22 años")
alumno2.set_matricula("3141577888") 

