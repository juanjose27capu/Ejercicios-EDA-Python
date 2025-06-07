import numpy as np

class lista:
    
    __elementos:np.array
    __tamaño:int
    __cantidad:int
    
    def __init__(self,tamaño):
        self.__elementos=np.empty(tamaño,dtype=int)
        self.__tamaño=tamaño
        self.__cantidad=0
    def vacia(self):
        return self.__cantidad==0
    def llena(self):
        return self.__cantidad==self.__tamaño
    def insertar(self,posicion,elemento):
        if not self.llena():
            if 1<=posicion<=self.__cantidad+1:
                tope=self.__cantidad
                while tope!=posicion-1:
                    self.__elementos[tope]=self.__elementos[tope-1]
                    tope-=1
                self.__elementos[posicion-1]=elemento
                self.__cantidad+=1
            else:
                raise ValueError("Posición Inválida")
        else:
            print("Lista Llena")
    def suprimir(self,posicion):
        if not self.vacia():
            if 1<=posicion<=self.__cantidad:
                tope=self.__cantidad
                while tope!=posicion-1:
                    self.__elementos[posicion-1]=self.__elementos[posicion]
                    posicion+=1
                self.__cantidad-=1
        else:
            print("Lista Vacía")
    def recuperar(self,posicion):
        if not self.vacia():
            if 1<=posicion<=self.__cantidad:
                return self.__elementos[posicion-1]
            else:
                raise ValueError("Posición Inválida")
        else:
            print("Lista Vacía")
    def buscar(self,elemento):
        if not self.vacia():
            i=0
            while i<self.__cantidad-1 and self.__elementos[i]!=elemento:
                i+=1
            if i<self.__cantidad-1:
                i+=1
            else:
                i=-1
            return i
        else:
            print("Lista Vacía")
    def primer_elemento(self):
        if not self.vacia():
            return self.__elementos[0]
        else:
            print("Lista Vacía")
    def ultimo_elemento(self):
        if not self.vacia():
            return self.__elementos[self.__cantidad-1]
        else:
            print("Lista Vacía")
    def siguiente(self,posicion):
        if not self.vacia():
            if 1<=posicion<self.__cantidad:
                return self.__elementos[posicion]
            else:
                raise ValueError("No es posible obtener el elemento siguiente por posición inválida o porque no existe")
        else:
            print("Lista Vacía")
    def anterior(self,posicion):
        if not self.vacia():
            if 1<posicion<=self.__cantidad:
                return self.__elementos[posicion-2]
            else:
                raise ValueError("No es posible obtener el elemento siguiente por posición inválida o porque no existe")
        else:
            print("Lista Vacía")        
    def recorrer(self):
        for i in range(0,self.__cantidad):
            print(self.__elementos[i],end=' ')
    def __add__(self,other):
        for i in range(0,self.__cantidad):
            print(self.__elementos[i]+other.__elementos[i],end=' ')
    def __sub__(self,other):
        for i in range(0,self.__cantidad):
            print(self.__elementos[i]-other.__elementos[i],end=' ')
    def __mul__(self,esc):
        for i in range(0,self.__cantidad):
            print(self.__elementos[i]*esc,end=' ')
if __name__=="__main__":
    
    p1=lista(4)
    p2=lista(4)
    p1.insertar(1,1)
    p1.insertar(2,4)
    p1.insertar(2,5)
    p1.insertar(4,2)
    p2.insertar(1,3)
    p2.insertar(1,4)
    p2.insertar(3,5)
    p2.insertar(4,6)
    print("Polinomio 1:")
    p1.recorrer()
    print("\nPolinomio 2:")
    p2.recorrer()
    print("\nSuma del polinomio 1 con el polinomio 2:\n")
    p1+p2
    print("\nResta del polinomio 1 con el polinomio 2:\n")
    p1-p2
    escalar=int(input("\nIngrese un escalar: "))
    print(f"Producto del polinomio 1 por {escalar}\n")
    p1*escalar
    print(f"\nProducto del polinomio 2 por {escalar}\n")
    p2*escalar