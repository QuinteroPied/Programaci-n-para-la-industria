import math
import numpy as np

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