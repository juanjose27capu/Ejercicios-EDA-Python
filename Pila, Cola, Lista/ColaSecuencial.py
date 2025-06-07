import numpy as np

class cola:
    __cola:np.array
    __inicio:int
    __final:int
    __capacidad:int
    __cantidad:int
    
    def __init__(self,capacidad):
        self.__cola=np.empty(capacidad,dtype=int)
        self.__inicio=0
        self.__final=0
        self.__capacidad=capacidad
        self.__cantidad=0
    def vacia(self):
        return self.__cantidad==0
    def llena(self):
        return self.__cantidad==self.__capacidad
    def insertar(self,elemento):
        if self.llena():
            raise Exception("ERROR: Cola LLena")
        self.__cola[self.__final]=elemento
        self.__final=(self.__final+1)%self.__capacidad
        self.__cantidad+=1
    def suprimir(self):
        if self.vacia():
            raise Exception("ERROR: Cola Vacía")
        elemento=self.__cola[self.__inicio]
        self.__cola[self.__inicio]=None
        self.__inicio=(self.__inicio+1)%self.__capacidad
        self.__cantidad-=1
        print(f"Elemento eliminado: {elemento}")
    def getInicio(self):
        return self.__cola[self.__inicio]
    def getFinal(self):
        return self.__cola[self.__final-1]
        