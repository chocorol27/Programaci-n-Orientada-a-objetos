class Figuras():
    def __init__(self, x,y,visible):
        self.x=x
        self.y=y
        self.visible=visible


    def esta_visible(self):
        return self.visible

    def mostar(self):
        self.visible=True
     

    def ocultar(self):
        self.visible=False
      

    def mover(self,nueva_x,nueva_y):
        self.x=nueva_x
        self.y=nueva_y

    def calcular_area(self):
        pass


class rectangulos(Figuras):
    def __init__(self,x,y,visible,altura,ancho):
        super().__init__(x,y,visible)
        self.__altura=altura
        self.__ancho=ancho

    def get_altura(self):
        return self.__altura
    def set_altura(self,altura):
        self.__altura=altura

    def get_ancho(self):
        return self.__ancho
    def set_ancho(self,ancho):
        self.__ancho=ancho


    def ocultar(self):
        self.visible=False

    def mostar(self):
        self.visible=True

    def clacular_area(self):
        return self.__altura * self.__ancho
    
class circulos(Figuras):
    def __init__(self,x,y,visible,radio):
        super().__init__(x,y,visible)
        self.__radio=radio

    def get_radio(self):
        return self.__radio
    def set_radio(self,radio):
        self.__radio=radio


    def ocultar(self):
        self.visible=False

    def mostar(self):
        self.visible=True

    def clacular_area(self):
        return 3.14 * (self.radio**2)
            
rectangulo1=rectangulos(3,4,True,10,20)
print(f"El area del rectangulo es: {rectangulo1.clacular_area()}")
circulo1=circulos(3,3,True,6)
print(f"El area del circulo es: {circulo1.clacular_area()}")