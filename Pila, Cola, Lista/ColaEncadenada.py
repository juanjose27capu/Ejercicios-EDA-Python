class nodo(object):
    __dato:int
    __sig:None
    
    def __init__(self,dato):
        self.__dato=dato
        self.__sig=None
    def getDato(self):
        return self.__dato
    def getSiguiente(self):
        return self.__sig
    def setSiguiente(self,siguiente):
        self.__sig=siguiente
    def setDato(self,dato):
        self.__dato=dato
        
class cola(nodo):
    __inicio:nodo
    __final:nodo
    __tamaño:int
    
    def __init__(self):
        self.__inicio=None
        self.__final=None
        self.__tamaño=0
    def vacia(self):
        return self.__inicio==None
    def agregar(self,dato):
        nuevonodo=nodo(dato)
        if self.vacia():
            self.__inicio=nuevonodo
        else:
            self.__final.setSiguiente(nuevonodo)
        self.__final=nuevonodo
        self.__tamaño+=1
    def suprimir(self):
        if self.vacia():
            raise Exception("ERROR: Cola Vacía")
        dato=self.__inicio.getDato()
        self.__inicio=self.__inicio.getSiguiente()
        if self.__inicio==None:
            print("La cola quedó vacía")
        self.__tamaño-=1
        print(f"Dato Eliminado: {dato}")
    def getDatoInicial(self):
        if self.vacia():
            raise Exception("ERROR: Cola Vacía")
        return self.__inicio.getDato()
    def __len__(self):
        return self.__tamaño
    
    
    