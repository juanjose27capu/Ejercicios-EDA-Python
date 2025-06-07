import random

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
        self.__tamaño-=1
        return dato
    def getDatoInicial(self):
        if self.vacia():
            raise Exception("ERROR: Cola Vacía")
        return self.__inicio.getDato()
    def __len__(self):
        return self.__tamaño
    
    
if __name__=="__main__":
    
    tiempo_atencion_cajero = 5
    frecuencia_llegada_clientes= 2
    tiempo_maximo_simulacion= 30
    cajero=0
     
    tiempo_espera_acumulado=0
    clientes_atendidos=0
     
    cola_cajeros=cola()
    reloj=0
     
    print("SIMULACION CAJERO:")
    
    while reloj < tiempo_maximo_simulacion:
         
        if (random.random())<=(1/frecuencia_llegada_clientes):
           
           cola_cajeros.agregar(reloj)
           print(f"Cliente llegó en el minuto {reloj}")
           
        if cajero==0 and not cola_cajeros.vacia():
           cliente=cola_cajeros.suprimir()
           tiempo_espera=reloj-cliente
           print(f"Cliente atendido en el minuto {reloj}, Tiempo de espera: {tiempo_espera} minutos")
           tiempo_espera_acumulado+=tiempo_espera
           clientes_atendidos+=1
           cajero=tiempo_atencion_cajero
       
        reloj+=1
        if cajero>0:
            cajero-=1

    tiempo_espera_promedio=tiempo_espera_acumulado/clientes_atendidos
    print(f"Tiempo de espera promedio de los clientes atendidos: {tiempo_espera_promedio:.2f} minutos")
        
    
        
        
            
                
                
     