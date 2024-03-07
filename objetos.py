
# para crear objetos la palabra clave es Class
from typing import Any
import math as math


class Persona: 
    # Esto se conoce como constructor de clase 
    def __init__(self, nombre:str, edad:int, pelicula_favorita:str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.pelicula_favorita = pelicula_favorita
    
    def presentarse(self):
        print(f"Buenas, que bonito es saludar y ser saludado, mi nombre es {self.nombre} tengo {self.edad} y mi película favorita es {self.pelicula_favorita}")

santiago = Persona('Carlos', edad=23, pelicula_favorita='Dragon Ball')
#print(santiago.presentarse())

class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def hacer_sonido(self):
        pass

class Perro(Animal):

    def hacer_sonido(self):
        print("Guauuuu")
    
class Gato(Animal):

    def hacer_sonido(self):
        print("Miauuuu")
    
gato = Gato('Vaquita') 
perro = Perro("Yessie")

#print(f"Mi gato se llama {gato.nombre} y hace {ato.hacer_sonido}")

#print(f"Mi perro se llama {perro.nombre} y hace {perro.hacer_sonido}")
#gato.hacer_sonido
#--------------------------------------------------------------------------------------------------------------#

class Figura: # Definimos la CLASE PADRE 
    def __init__(self, color) -> None: # Definimos el o los atributos
        self.color=color # autoretribuimos los valores
    def calcular_area(self): # Definimos el método
        pass

class Rectangulo(Figura): # Definimos el objeto
    def __init__(self, color, altura, base) -> None: # Definimos el atributo
        super().__init__(color) # Así nos traemos el atributo de la CLASE PADRE
        self.altura = altura # autoretribuimos los valores
        self.base = base # autoretribuimos los valores
    def calcular_area(self):   # Método
        area = self.base*self.altura
        return area
    
class Circulo(Figura): # Definimos el objeto
    def __init__(self, color, radio) -> None: # Definimos el atributo
        super().__init__(color) # Así nos traemos el atributo de la CLASE PADRE
        self.radio = altura # autoretribuimos los valores
    def calcular_area(self):   # Método
        area = self.radio*(math.pi**2)
        return area
    
class Triangulo(Figura): # Definimos el objeto
    def __init__(self, color, altura, base) -> None: # Definimos el atributo
        super().__init__(color) # Así nos traemos el atributo de la CLASE PADRE
        self.altura = altura # autoretribuimos los valores
        self.base = base # autoretribuimos los valores
    def calcular_area(self):   # Método
        area = (self.base*self.altura)/2
        return area

rectangulo=Rectangulo(color="rojo", altura=10, base=5)
print(rectangulo.calcular_area())

#-----------------------------------------------------------------------------------------------------------------#

class Cuenta_Bancaria:
    def __init__(self, titular, saldo_inicial) -> None:
        self.titular=titular
        self._saldo=saldo_inicial
        
    def depositar(self, cantidad):
        self._saldo += cantidad
        print('el saldo actual es de '+str(self._saldo))
    def retirar(self, cantidad):
        if cantidad >0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            print('retiro exitoso, el saldo actual es: '+str(self._saldo))

    def obtener_saldo(self):
        return self._saldo
    
    cuenta_carlos=Cuenta_Bancaria(titular='Carlos Quintero', saldo_inicial=5000)