
# para crear objetos la palabra clave es Class
from typing import Any


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
        return "Guau"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
gato = Gato('Vaquita')
perro = Perro("Yessie")

print(f"Mi gato se llama {gato.nombre} y hace {gato.hacer_sonido}")

print(f"Mi perro se llama {perro.nombre} y hace {perro.hacer_sonido}")