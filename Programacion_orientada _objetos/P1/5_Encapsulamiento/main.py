#instanciar los objetos para posteriotrmente usarlos
from coches import Coches
num_coches=int(input("Cuantos coches deseas crear?"))
for i in range(0,num_coches):
    print(f"n\t....Datos del coche 1 {i+1}....\n")
    marca=input("Ingresa la marca").upper()
    color=input("Ingresa el color").upper()
    modelo=input("ingresa el modelo").upper()
    velocidad=int(input("ingresa el modelo")).upper()
    potencia=int(input("Ingresa la potencia"))
    plazas=int(input("Ingresa el numero de plazas"))
    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)
    print((f"datos del coche 1: \n marca:{coche1.get_marca()}\n color:{coche1.get_color()} \n modelo:{coche1.get_modelo()}\n velocidad:{coche1.get_velocidad()} \n caballaje:{coche1.get_caballaje()}\n plazas:{coche1.get_plazas()}"))
'''
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
print(f"El coche 1 es un {coche1.marca} de color {coche1.color} y su velocidad es {coche1.velocidad}km/h y su ")
print(f"El coche 2 es un {coche2.marca} de color {coche2.color} y su velocidad es {coche2.velocidad}km/h y su ")
'''
