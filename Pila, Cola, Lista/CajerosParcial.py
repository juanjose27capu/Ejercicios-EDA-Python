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

    frecuencia_clientes=3
    tiempo_cajero1=4
    tiempo_cajero2=5

    cajero1=0
    cajero2=0

    cola_cajeros=cola()
    tms=30
    reloj=0

    clientes_atendidos=0
    tiempo_espera_acumulado=0

    while reloj<tms:

        if random.random()<=(1/frecuencia_clientes):
            cola_cajeros.agregar(reloj)
            print(f"Ingresó un cliente en el minuto {reloj}")

        if cajero1==0 and not cola_cajeros.vacia():

            cliente=cola_cajeros.suprimir()
            tiempo_espera=reloj-cliente
            tiempo_espera_acumulado+=tiempo_espera
            clientes_atendidos+=1
            print(f"Cliente atendido en el minuto {reloj} por Cajero 1, Tiempo de espera: {tiempo_espera} minutos")
            cajero1+=tiempo_cajero1

        elif cajero2==0 and not cola_cajeros.vacia():

            cliente=cola_cajeros.suprimir()
            tiempo_espera=reloj-cliente
            tiempo_espera_acumulado+=tiempo_espera
            clientes_atendidos+=1
            print(f"Cliente atendido en el minuto {reloj} por Cajero 2, Tiempo de espera: {tiempo_espera} minutos")
            cajero2+=tiempo_cajero2

        if cajero1>0:
            cajero1-=1
        if cajero2>0:
            cajero2-=1
        reloj+=1

    tiempo_espera_promedio=tiempo_espera_acumulado/clientes_atendidos
    print(f"Tiempo de espera promedio: {tiempo_espera_promedio:.2f} minutos")
    print(f"Clientes atendidos en {tms} minutos: {clientes_atendidos}")
