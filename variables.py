import math
import pandas



# aprendamos sobre variables
def suma(a,b):
    #"esto hace una suma"
    return a+b

print(suma(7,3))

lista = [2,3,4,'valor',45.5,False,10]
print(lista[0])
print(len('la longuitud de esta lista es :'))

lista.append('ultimovalor') # agregamos un valor a lo ultimo de la lista
print(lista)


lista[0]=7 #cambio lo que hay en el primer valor (0) por el valor de 7
print(lista)

listaduplicados=[repr]


# identacion y documentacion de funciones
def sum(num1:float, num2:float) -> float:
    """esta función suma dos numeros 

    Args:
        num1 (float): este es el numero 2
        num2 (float): este es el numero 2

    Returns:
        float: retorna la suma 
    """
    valor_suma=num1+num2
    return valor_suma

print(sum(2,2))

