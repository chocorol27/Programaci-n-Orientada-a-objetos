#instanciar los objetos para posteriotrmente usarlos
from coches import *
import os

def borrarPantalla():
    os.system("cls")

def esperaTecla():
    input(".....iprima una tecla para continuar....")
def datos_autos():
    borrarPantalla()
    print(f"\t....Datos del coche ....\n")
    marca=input("Ingresa la marca:").upper()
    color=input("Ingresa el color:").upper()
    modelo=input("ingresa el modelo:").upper()
    velocidad=int(input("ingresa la velocidad:"))
    potencia=int(input("Ingresa la potencia:"))
    plazas=int(input("Ingresa el numero de plazas:"))
    return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculos(marca,color,modelo,velocidad,potencia,plazas):
    print(f"\n\Datos del vehiculo:\n Marca:{marca} \n color:{color} \n modelo:{modelo} \n velocidad:{velocidad} \n potencia:{potencia} \n plazas{plazas}")


def autos():
    print(f"\t....ingresa los natos del vehiculo ....\n")
    marca,color,modelo,velocidad,potencia,plazas=datos_autos()
    coche=Coches(marca,color,modelo,velocidad,potencia,plazas)
    imprimir_datos_vehiculos(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.potencia,coche.plazas)

    
    
def camionetas():
    print(f"\t....Datos de la camioneta  ....\n")
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    camioneta=Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)

    traccion=input("Ingresa el tipo de traccion (4x4/4x2):").upper().strip()
    cerrada=input("Ingresa si es cerrada o no (Si/No):").upper().strip()
    if cerrada=="Si":
        cerrada=True
    else:
        cerrada=False
    imprimir_datos_vehiculos(camioneta.marca,camioneta.color,camioneta.modelo,camioneta.velocidad,camioneta.potencia,camioneta.plazas)
    print(f"Su traccion es{camioneta.traccion}y la es {camioneta.cerrada} ")
def camiones():
    print(f"\t....Datos del camion  ....\n")
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camion")
    eje=int(input("Ingresa el numero de ejes:"))
    capacidad_carga=int(input("Ingresa la capacidad de carga en toneladas:"))
   
    camion=Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidad_carga)
    print(f"Datos del vehiculo:\n Marca:{camion.marca} \n Color:{camion.color} \nModelo:{camion.modelo} \n Velocidad:{camion.velocidad} \n Potencia:{camion.potencia} \n Plazas:{camion.plazas} \n Ejes:{camion.eje} \n Capacidad de carga:{camion.capacidad_carga}")  




def main():
    opcion=True
    while opcion:
        os.system("cls")
        opcion=input("\n\t\t....Menu Principal....\n1.-Autos\n2.-Camionetas\n3.-Camiones\n4.-Salir\n\tElige una opccion:").lower().strip()
        match opcion:
            case "1":
            
                print("\n\t....Autos....\n")
                autos()
                esperaTecla()
            case "2":
         
                print("\n\t....Camionetas....\n")
                camionetas()
                esperaTecla()
            case "3":
           
                camiones()
                esperaTecla()
            case "4":
                borrarPantalla()
                print("Gracias por usar el programa")
                
                opcion=False
            case _:
                input("Opcion no valida")
         
if __name__=="__main__":
    main()
