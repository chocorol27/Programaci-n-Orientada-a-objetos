import os 
os.system("cls")
#Clase coches
class Coches:
    #metodo constructor que inicializa los valores cuando se instancia un objeto
    #de la clase
    def __init__(self,color,marca,velocidad):
        self.color=color
        self.marca=marca
        self.velocidad=velocidad
     #Metodos del objeto
    def acelerar(self,incremento):
        self.velocidad=self.velocidad+incremento
        return self.velocidad
    
    def frenar(self,decremento):
        self.velocidad=self.velocidad-decremento
        return self. velocidad
    
    def tocar_claxon(self):
        print("piiiiiiii")
        pass


#Instanciar un objeto de la clase Coches
coche1=Coches("Blanco","Toyota",220)
coche2=Coches("Amarillo","Nissan",120)

print(f"Los valores del obejto 1 son:{coche1.marca},{coche1.color},{coche1.velocidad}")
print(f"El coche 1 acelera a :{coche1.velocidad}km/h a {coche1.acelerar(50)}km/h")
print(f"El coche 2 frena a :{coche2.velocidad}km/h a {coche2.frenar(100)}km/h")
print(f"Los valores del obejto 2 son:{coche2.marca},{coche2.color},{coche2.velocidad}")
print(coche1.tocar_claxon())