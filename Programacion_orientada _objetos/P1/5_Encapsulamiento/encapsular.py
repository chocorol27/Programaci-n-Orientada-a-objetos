''' en un pilar de pooo que permite indicar cual es la manera de como poder
utilizar los atributo y metodos de una clase a la hora de usar en objetos o en herecia'''
import os
os.system("cls")

class Clase:
    atributo_publico="Soy un publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"
    
    def __init__(self,color,tamanio):
        self.__color=color
        self.__tamanio=tamanio

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self,tamanio):
        self.__tamanio=tamanio

    @property
    def atributopublico(self):
        return self.atributo_publico
    
    @atributopublico.setter
    def atributopublico(self,atributo_publico):
        self.atributopublico=atributo_publico

    @property
    def atributo_protegido(self):
        return self._atributo_protegido

    @atributo_protegido.setter
    def atributo_protegido(self,atributo_protegido):
        self._atributo_protegido=atributo_protegido

    @property
    def atributo_privado(self):
        return self.__atributo_privado

    @atributo_privado.setter
    def atributo_privado(self,atributo_privado):
        self.__atributo_privado=atributo_privado




    
    #lo mas comun para usar un atributo privado es por medio de una funcion dentro de la clase
    #Ejemplo
    def getAtributoPrivado(self):
        return self.__atributo_privado

#Utilizar la clase 
objeto=Clase("Rojo","Grande")
print(objeto.atributopublico)
print(objeto.atributo_protegido)
print(objeto.atributo_privado)
objeto.color="Azul"
print(objeto.color)
#print(objeto.__atributo_privado)no se pueden usar fuera de la clase en cambio los protegidos y publicos si se puede
