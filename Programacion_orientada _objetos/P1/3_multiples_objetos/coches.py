class Coches:
    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0
    ''''
    Crear los metodos stter y getters estos metodos son importantes y necesarios en todas las 
    clases para que el programador interactue con los valores de los atributos a traves de stostos metodos
    digamos que es la manera mas adecuada y recomendada para solivitar un valor get y o para ingresar o cambiar
    un valor set a un atributo en particular de la clase a traves de un objeto.
    En teoria se deberia crear un metodo getters y setters por cada atributo
   '''
    def get_marca(self):
        return self.__marca
    #segunda forma get
    @property  
    def marca(self):
        return self.__marca
    #setter
    @marca.setter
    def marca(self,marca):
        self.__marca=marca

    ##########
    def set_marca(self,marca):
        self.__marca=marca
    
    def get_color(self):
        return self.__color
    def set_color(self,color):
        self.__color=color
    
    def get_velocidad(self):
        return self.__velocidad
    def set_velocidad(self,velocidad):
        self.__velocidad=velocidad

    def get_caballaje(self):
        return self.__caballaje
    def set_caballaje(self,caballaje):
        self.__caballaje=caballaje

    def get_plazas(self):
        return self.__plazas
    def set_plazas(self,plazas):
        self.__plazas=plazas
    
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self,modelo):
        self.__modelo=modelo
                   


    def acelerar(self):
        return "El coche esta acelerando"
    def frenar(self):
        return "El coche esta frenando"
#multiples objetos crear dos o mas objetos a traves del mismo molde(clase)
coche1=Coches()
coche1.marca="VW"
coche1.set_color("Blanco")
coche1.set_modelo("2022")
coche1.set_velocidad(220)
coche1.set_caballaje(150)
coche1.set_plazas(5)

print((f"datos del coche 1: \n marca:{coche1.get_marca()}\n color:{coche1.get_color()} \n modelo:{coche1.get_modelo()}\n velocidad:{coche1.get_velocidad()} \n caballaje:{coche1.get_caballaje()}\n plazas:{coche1.get_plazas()}"))

coche2=Coches()
coche2.set_marca("Audi")
coche2.set_color("Rojo")
coche2.set_modelo("2023")
coche2.set_velocidad(280)
coche2.set_caballaje(200)
coche2.set_plazas(4) 


print((f"datos del coche 2: marca:{coche2.get_marca()} color:{coche2.get_color()} modelo:{coche2.get_modelo()} velocidad:{coche2.get_velocidad()} caballaje:{coche2.get_caballaje()} plazas:{coche2.get_plazas()}"))
'''print(f"El coche 1 es un {coche1.marca} de color {coche1.color} y su velocidad es {coche1.velocidad}km/h y su ")
print(f"El coche 2 es un {coche2.marca} de color {coche2.color} y su velocidad es {coche2.velocidad}km/h y su ")'''
