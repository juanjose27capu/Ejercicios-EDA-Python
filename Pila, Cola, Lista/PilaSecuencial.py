import numpy as np

class pila:
    __elementos:np.array
    __cantidad:int
    __tope:int
    
    def __init__(self,dimension):
        self.__elementos=np.empty(dimension,dtype=int)
        self.__cantidad=dimension
        self.__tope=0
    def vacia(self):
        return self.__tope==0
    def insertar(self,elemento):
        if self.__tope<self.__cantidad:
            self.__elementos[self.__tope]=elemento
            self.__tope+=1
        else:
            print("No es posible insertar el elemento: Pila Llena")
    def recorrer(self):
        i=self.__tope-1
        while i>=0:
            print(f"|{self.__elementos[i]}|")
            i-=1
    def surpimir(self):
        if not self.vacia():
            self.__tope-=1
        else:
            print("La pila esta vacía, no hay elementos para eliminar")
    def getTope(self):
        return self.__tope
    def getCantidad(self):
        return self.__cantidad
    def getElementos(self):
        return self.__elementos