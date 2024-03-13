
# un prestamo es una relacion entre un usuario y un libro y tiene una fecha de prestamo y una fecha de vencimiento
# Clases: Libro  -> # cada libro tiene titulo, autor y estado (disponible-prestado) - metodo para cambiar el estado del libro
# Clases: Usuario -> # cada usuario tiene un identificador y un nombre unico - metodo para mostrar la informacion del usuario
# Clases: Prestamo -> # libro prestado, fecha de prestamo y fecha de vencimiento - metodo para mostrar la información del prestamo y calcular si el prestamo está vencido o no.
# Clases: Biblioteca -> # Libros, usuarios y prestamos - metodo para agregar y eliminar libros, usuarios , realizar prestamos y devoluciones y buscar libros disponibles.

from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.estado = "Disponible"

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_info(self):
        print(f"Libro: {self.titulo} - Autor: {self.autor} - Estado: {self.estado}")

class Usuario:
    def __init__(self, nombre, identificador):
        self.nombre = nombre
        self.identificador = identificador

    def mostrar_info(self):
        print(f"Usuario: {self.nombre} - ID: {self.identificador}")

class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_vencimiento = self.fecha_prestamo + timedelta(days=14)

    def mostrar_info(self):
        print(f"Prestamo - Libro: {self.libro.titulo} - Usuario: {self.usuario.nombre}")
        print(f"Fecha de Préstamo: {self.fecha_prestamo.strftime('%Y-%m-%d')}")
        print(f"Fecha de Vencimiento: {self.fecha_vencimiento.strftime('%Y-%m-%d')}")

    def esta_vencido(self):
        return datetime.now() > self.fecha_vencimiento

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self.usuarios.remove(usuario)

    def realizar_prestamo(self, libro, usuario):
        if libro.estado == "Disponible":
            nuevo_prestamo = Prestamo(libro, usuario)
            libro.cambiar_estado("Prestado")
            self.prestamos.append(nuevo_prestamo)
            print("Préstamo realizado con éxito.")
        else:
            print("El libro no está disponible para préstamo.")

    def realizar_devolucion(self, prestamo):
        prestamo.libro.cambiar_estado("Disponible")
        self.prestamos.remove(prestamo)
        print("Devolución realizada con éxito.")

    def buscar_libros_disponibles(self):
        libros_disponibles = [libro for libro in self.libros if libro.estado == "Disponible"]
        if libros_disponibles:
            print("Libros disponibles:")
            for libro in libros_disponibles:
                libro.mostrar_info()
        else:
            print("No hay libros disponibles en este momento.")

# Programa principal
if __name__ == "__main__":
    biblioteca = Biblioteca()

    libro1 = Libro("La Sombra del Viento", "Carlos Ruiz Zafón")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")

    usuario1 = Usuario("Chat", 1)
    usuario2 = Usuario("Piti", 2)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_usuario(usuario1)
    biblioteca.agregar_usuario(usuario2)

    biblioteca.buscar_libros_disponibles()

    biblioteca.realizar_prestamo(libro1, usuario1)

    biblioteca.buscar_libros_disponibles()

    biblioteca.realizar_devolucion(biblioteca.prestamos[0])

    biblioteca.buscar_libros_disponibles()
