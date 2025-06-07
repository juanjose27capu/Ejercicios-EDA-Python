class nodo:
    __dato:int
    __sig:int
    
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
        
class pila:
    
    __tope:nodo
    __cant:int
    
    def __init__(self):
        self.__tope=None
        self.__cant=0
    def vacia(self):
        return self.__cant==0
    def insertar(self,elemento):
        nuevo=nodo(elemento)
        nuevo.setSiguiente(self.__tope)
        self.__tope=nuevo
        self.__cant+=1
    def suprimir(self):
        if not self.vacia():
            self.__tope=self.__tope.getSiguiente()
            self.__cant-=1
        else:
            print("Error: La Pila está vacía")
    def recorrer(self):
        if self.vacia():
            print("Pila Vacía")
        else:
            aux=self.__tope
            while aux!=None:
                print(aux.getDato())
                aux=aux.getSiguiente()

    def factorial(self, numero):
        
        while numero>0:
            self.insertar(numero)
            numero-=1
        numfact=1
        while not self.vacia():
            aux=self.__tope
            numfact*=aux.getDato()
            self.suprimir()
        return numfact
    

if __name__=="__main__":
    unapila=pila()
    numero=int(input("Ingrese un numero mayor a 0 para calcular su factorial: "))
    resultado= unapila.factorial(numero)
    print(f"{numero}! = {resultado}")