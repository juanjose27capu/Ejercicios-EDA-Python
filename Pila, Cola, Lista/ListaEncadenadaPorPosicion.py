class nodo:
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

class lista(nodo):

    __cabeza: nodo
    __cantidad: int

    def __init__(self):
        self.__cabeza=None
        self.__cantidad=0
    def vacia(self):
        return self.__cantidad==0
    def insertar(self,posicion,elemento): 
        
        if 1<=posicion<=self.__cantidad+1:
            nuevonodo=nodo(elemento)
            if posicion==1:
                nuevonodo.setSiguiente(self.__cabeza)
                self.__cabeza=nuevonodo
            else:
                i=1
                aux=self.__cabeza
                while i<posicion-1:
                    aux=aux.getSiguiente()
                    i+=1
                nuevonodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nuevonodo)
            self.__cantidad+=1
        else:
            print("Posición inválida")
    def suprimir(self,posicion):
        if not self.vacia():
            if 1<=posicion<=self.__cantidad+1:

                if posicion==1:
                    dato=self.__cabeza.getDato()
                    aux=self.__cabeza.getSiguiente()
                    del(self.__cabeza)
                    self.__cabeza=aux
                else:
                    i=1
                    aux=self.__cabeza
                    while i<posicion:
                        anterior=aux
                        aux=aux.getSiguiente()
                        i+=1
                    dato=aux.getDato()
                    anterior.setSiguiente(aux.getSiguiente())
                    del(aux)
                self.__cantidad-=1
                print(f"Dato eliminado en la posicion {posicion}: {dato}")
            else:
                raise ValueError("Posición inválida")   
        else:
            print("Lista Vacía")
    def recuperar(self,posicion):
        
        if not self.vacia():
            if 1<=posicion<=self.__cantidad:
                aux=self.__cabeza
                i=1
                while i<posicion:
                    aux=aux.getSiguiente()
                    i+=1
                return aux.getDato()
            else:
                raise ValueError("Posición inválida")
        else:
            print("Lista Vacía")
    def buscar(self,elemento): #Devuelve la posicion del elemento que se busca
        
        i=0
        aux=self.__cabeza
        while i<self.__cantidad and aux.getDato()!=elemento:
            aux=aux.getSiguiente()
            i+=1
        if i<self.__cantidad:
            i+=1
        else:
            i=-1
        return i
    def primer_elemento(self):
        if not self.vacia():
            return self.__cabeza.getDato()
        else:
            print("Lista Vacía")
    def ultimo_elemento(self):
        if not self.vacia():
            aux=self.__cabeza
            while aux.getSiguiente()!=None:
                aux=aux.getSiguiente()
            return aux.getDato()
        else:
            print("Lista Vacía")
    def siguiente(self,posicion):
        if not self.vacia():
            if 1<=posicion<self.__cantidad:
                i=1
                aux=self.__cabeza
                while i<=posicion:
                    aux=aux.getSiguiente()
                    i+=1
                return aux.getDato()
            else:
                raise ValueError("Posición Inválida: No se puede obtener el dato siguiente")
        else:
            print("Lista Vacía")
    def anterior(self,posicion):
        if not self.vacia():
            if 1<posicion<=self.__cantidad:
                i=1
                aux=self.__cabeza
                while i<posicion-1:
                    aux=aux.getSiguiente()
                    i+=1
                return aux.getDato()
            else:
                raise ValueError("Posición Inválida: No se puede obtener el dato anterior")
        else:
            print("Lista Vacía")
    def recorrer(self):
        aux=self.__cabeza
        while aux.getSiguiente()!=None:
            print(aux.getDato())
            aux=aux.getSiguiente()
        print(aux.getDato())
    
        