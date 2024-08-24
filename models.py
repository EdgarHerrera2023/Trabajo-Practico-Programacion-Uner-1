

# models.py
import json
from typing import List

class Libro:
    def __init__(self, id_libro, titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion
        self.genero = genero
        self.cantidad_disponible = cantidad_disponible

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Libro(**data)

class Socio:
    def __init__(self, id_socio, nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono):
        self.id_socio = id_socio
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.correo_electronico = correo_electronico
        self.telefono = telefono

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Socio(**data)

class Prestamo:
    def __init__(self, id_prestamo, id_socio, id_libro, fecha_prestamo, costo, fecha_devolucion, estado_prestamo):
        self.id_prestamo = id_prestamo
        self.id_socio = id_socio
        self.id_libro = id_libro
        self.fecha_prestamo = fecha_prestamo
        self.costo = costo
        self.fecha_devolucion = fecha_devolucion
        self.estado_prestamo = estado_prestamo

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Prestamo(**data)

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
