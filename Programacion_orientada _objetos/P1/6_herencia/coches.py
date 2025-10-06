class Coches:
    ##Metodo constructor con este metodo se inicializa a un objeto con unos valores iniciales
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas
        
    
   
    @property
    def marca(self):
        return self._marca
    #setter
    @marca.setter
    def marca(self,marca):
        self._marca=marca

    @property
    def color(self):
        return self._color
    #setter
    @color.setter
    def color(self,color):
        self._color=color

    @property
    def modelo(self):
        return self._modelo
    #setter
    @modelo.setter
    def marca(self,modelo):
        self._modelo=modelo

    @property
    def velocidad(self):
        return self._velocidad
    #setter
    @velocidad.setter
    def marca(self,velocidad):
        self._velocidad=velocidad

    @property
    def caballaje(self):
        return self._caballaje
    #setter
    @caballaje.setter
    def marca(self,caballaje):
        self._caballaje=caballaje

    def acelerar(self):
        return "El cocche esta acelerando"
    def frenar(self):
        return "El coche freno"
    
class Camiones(Coches):
        def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,eje,tipo_carga):
            super().__init__(marca,color,modelo,velocidad,caballaje,plazas)
            self._eje=eje
            self._tipo_carga=tipo_carga
        @property
        def eje(self):
            return self._eje
    #setter
        @eje.setter
        def eje(self,eje):
            self._eje=eje
        @property
        def tipo_carga(self):
            return self._tipo_carga
        @tipo_carga.setter
        def tipo_carga(self,tipo_carga):
            self._tipo_carga=tipo_carga





class Camionetas(Coches):
        def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
            super().__init__(marca,color,modelo,velocidad,caballaje,plazas)
            self._traccion=traccion
            self._cerrada=cerrada

        @property
        def traccion(self):
            return self._traccion
    #setter
        @traccion.setter
        def traccion(self,traccion):
            self._traccion=traccion

        @property
        def cerrada(self):
            return self._cerrada
        @cerrada.setter
        def cerrada(self,cerrada):
            self._cerrada=cerrada

        def transporte(self,num_pasajeros):
            self._num_pasajeros=num_pasajeros

