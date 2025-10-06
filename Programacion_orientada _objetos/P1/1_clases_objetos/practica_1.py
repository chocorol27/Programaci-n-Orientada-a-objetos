
import os
os.system("cls")
def area_rectangulo(base, altura):
    area=base*altura
    return area
print(area_rectangulo(5,10))


class AreaRectangulo:
    def areaRectangulo(self,base,altura):
        area=base*altura
        return area
rectangulo=AreaRectangulo() #Instanciar un objeto de la clase AreaRectangulo
print(f"El Area del rectangulo es :{rectangulo.areaRectangulo(5,10)}")


class AreaRectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def areaRectangulo(self):
        area=self.base*self.altura
        return area
rectangulo=AreaRectangulo(5,6) #Instanciar un objeto de la clase AreaRectangulo
print(f"El Area del rectangulo es :{rectangulo.areaRectangulo()}")