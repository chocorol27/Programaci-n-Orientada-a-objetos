class Coches:
    marca=""
    color=""
    velocidad=0
    caballaje=0
    plazas=0
    def acelerar(self):
        pass
    def frenar(self):
        pass
    
    
coche1=Coches()
coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5
coche2=Coches()
coche2.marca="Audi"
coche2.color="Rojo"
coche2.modelo="2020"
coche2.velocidad=280
coche2.caballaje=300
coche2.plazas=5

print(f"El coche 1 es un {coche1.marca} de color {coche1.color} y su velocidad es {coche1.velocidad}km/h y su ")
print(f"El coche 2 es un {coche2.marca} de color {coche2.color} y su velocidad es {coche2.velocidad}km/h y su ")
