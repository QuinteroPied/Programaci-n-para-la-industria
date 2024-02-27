import math

#Aprendamos sobre variables
#El lado izquierdo de la variable se conoce como identificador, el sìmbolo en la mitad (=) se conoce como sìmbolo de asignaciòn y
#me asigna al espacio de memoria identificado con el nombre de la variable el valor que se encuentra a la derecha
x = 20

#Tenemos los tipos de datos, string, integer, float, and bool. Estos se conocen como
#Tipo de dato de dato primario

nombre = 'Santiago' #Esto es un str
edad = 20 #Es un tipo de dato Integer Int
estatura = 1.99 #Es un tipo Float
is_profesor = True #Es tipo bool (False)

apellido = 'Echeverri'

nombre_completo = nombre + ' ' + apellido

Listas = [1,'valor',3,False,4,5.6 ] #Las listas son mutables

Listas[0]= 2

tuplas = (1,'valor', 3 , True, 2.1) #Las tuplas son inmutables


conjuntos = {1,2,3,4,5,5,5,5,5,5,5,5,5,5}

#dada la lista lista_con_dup  = [1,1,2,2,3,4,5,6,6,6] construir una lista con los mismos valores de 
#lista_con_dup pero sin duplicados hint: use la funciòn list y set 

lista_con_dup = [1,1,2,2,3,4,5,6,6,6]
 
nodubs= list(set(lista_con_dup))  #Con esto eliminamos los duplicados del arreglo

diccionarios = {
    'nombre': 'Santiago',
    'apellido': 'Echeverri',
    'Profesion': 'Matemático',
    'Ocupasión': 'Líder De Ingeniería de datos'
}


#for key in diccionarios.keys():
#    print(key)

def suma(num_1: float, num_2: float) -> float:

    """Suma dos nùmeros flotantes

    Args:
        num_1 (float): primer numero para ser sumado
        num_2 (float): Segundo numero para ser sumado

    Returns:
        float: Resultado de la suma de los nùmeros anteriores
    """
    valor_suma: float = num_1 + num_2
    return valor_suma

#Ejercicio: Escribir una función que muestre por pantalla 'Hola Mundo'

def hola_mundo() -> None:
    print('Hola Mundo')

##Ejercicio: Escribir una función que reciba el nombre de una persona y muestre por pantalla 'Hola (nombre)' 

def saludo(nombre:str) -> None:
    
    saludo = f"Hola {nombre}"
    print(saludo)

saludo('Pepito')

#Escribir una fución que reciba un número entero y devuelva su factorial. nótese que esta funci´pon si tiene return


def factorial(numero: int) -> int:
    """Esta funciòn calcula el factorial de un número dado

    Args:
        numero (int): número para tener facvtorial

    Returns:
        int: Valor del factorial
    """
    numero_factorial = math.factorial(numero)
    return numero_factorial

#Escribir una funciòn que reciba una lista de números y retorne su media

def mean(arrayList:list):
  return (np.array(arrayList)).mean()

def media(lista_numeros: list) -> float:
    media_valores = sum(lista_numeros)/len(lista_numeros)