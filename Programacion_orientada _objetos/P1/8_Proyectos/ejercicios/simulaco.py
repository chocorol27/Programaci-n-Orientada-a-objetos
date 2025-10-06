'''
Realizar un programa en el cual se declaren dos valores enteros por teclado
utilizando el metodo __init__ .Calcular despues la suma,resta,multiplicacion y division
utilizar un metodo para cada una e imprimir los resultados obtenidos
llamar la clase calculadora
'''
'''
class Calculadora:
    def __init__(self,num1,num2):
        self._num1=num1
        self._num2=num2
    
    @property
    def num1 (self):
        return self._num1
    @num1.setter
    def num1(self,num1):
        self._num1=num1

    @property
    def num2 (self):
        return self._num1
    @num1.setter
    def num2(self,num2):
        self._num2=num2


    def suma(self):
        return self._num1+self._num2'''



class Calculadora:
    def __init__(self):
        self._numero1=int(input("Ingresa el primer numero:"))
        self._numero2=int(input("Ingresa el segundo numero:"))

    @property
    def numero1(self):
        return self._numero1
    @numero1.setter
    def numero1(self,numero1):
        self._numero1=numero1
    @property
    def numero2(self):
        return self._numero2
    @numero2.setter
    def numero2(self,numero2):
        self._numero2=numero2

    def suma(self):
        return  self._numero1+self._numero2
    
    def resta(self):
        return self._numero1-self._numero2
    
    def multiplicacion(self):
        return self._numero1*self._numero2
    def division(self):
        return self._numero1/self._numero2
    
operacion=Calculadora() 
print(operacion.suma())
print(f"{operacion.numero1}+{operacion.numero2}={operacion.suma()}" )
print(operacion.multiplicacion())
print(operacion.division())

