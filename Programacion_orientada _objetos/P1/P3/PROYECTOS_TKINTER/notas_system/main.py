"""
1.-paradigma oo
2.-implementar mvc
3.-app de escritorio con interfaz grafica
"""
from tkinter import *
from view import vista

class App:
    def __init__(self, ventana):
        view = vista.View(ventana)

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()
    ventana.title("Sistema de Notas")