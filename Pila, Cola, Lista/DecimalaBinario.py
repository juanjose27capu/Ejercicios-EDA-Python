from PilaSecuencial import pila


def convertirnumero(numdecimal,unapila:pila):
    if numdecimal!=0:
        while numdecimal>=1:
            unapila.insertar((numdecimal%2))
            numdecimal/=2





if __name__=="__main__":
    
    unapila=pila(10)
    numerodecimal=int(input("Ingrese el numero decimal para convertir a binario: "))
    convertirnumero(numdecimal=numerodecimal,unapila=unapila)
    print(f"Numero {numerodecimal} convertido a binario con éxito")
    unapila.recorrer()