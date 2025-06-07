import random
class nodo(object):
    __dato:list
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
    
    tiempo_atencion_impresora = 5
    frecuencia_llegada_trabajos= 2
    tiempo_maximo_simulacion= 20
    impresora=0
     
    tiempo_espera_acumulado=0
    trabajos_atendidos=0
     
    cola_trabajos=cola()
    reloj=0
    reloj_impresion=0
    
    print("SIMULACION IMPRESORA:")
    
    while reloj < tiempo_maximo_simulacion:
        
        if (random.random())<=(1/frecuencia_llegada_trabajos):
            
            t=random.randint(1, 8)
            r=reloj
            cola_trabajos.agregar([r,t])
            print(f"Trabajo de {t} minutos llegó en el minuto {r}")
           
        if impresora==0 and not cola_trabajos.vacia():
            l=cola_trabajos.suprimir()
            trabajo,tiempo_impresion=l[0],l[1]
            tiempo_espera=reloj-trabajo
            print(f"Trabajo de {tiempo_impresion} minutos atendido en el minuto {reloj}, Tiempo de espera: {tiempo_espera} minutos")
            tiempo_espera_acumulado+=tiempo_espera
            trabajos_atendidos+=1
            impresora=tiempo_atencion_impresora
        if tiempo_impresion>tiempo_atencion_impresora:
            reloj_impresion+=1
        if reloj_impresion==5:
            print(f"Trabajo de {tiempo_impresion} minutos: Duración mayor a 5 minutos, se volvió a insertar en la cola")
            tiempo_impresion-=5
            cola_trabajos.agregar([reloj,tiempo_impresion])
            print(f"Nueva duración: {tiempo_impresion} minutos")
            reloj_impresion=0
            impresora=0
        reloj+=1
        if impresora>0:
            impresora-=1

    tiempo_espera_promedio=tiempo_espera_acumulado/trabajos_atendidos
    print(f"Cantidad de trabajos sin atender: {len(cola_trabajos)}")
    print(f"Tiempo de espera promedio de los trabajos atendidos: {tiempo_espera_promedio:.2f} minutos")
    
    
