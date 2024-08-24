# controllers.py
from models import Libro, Socio, Prestamo, load_data, save_data

LIBROS_FILE = 'data/libros.json'
SOCIOS_FILE = 'data/socios.json'
PRESTAMOS_FILE = 'data/prestamos.json'

def get_next_id(data: list) -> int:
    if data:
        return max(item['id_libro'] for item in data) + 1
    return 1

# Gestión de libros
def registrar_libro(libro: Libro):
    libros = load_data(LIBROS_FILE)
    libro.id_libro = get_next_id(libros)
    libros.append(libro.to_dict())
    save_data(LIBROS_FILE, libros)

def editar_libro(id_libro: int, libro: Libro):
    libros = load_data(LIBROS_FILE)
    for idx, item in enumerate(libros):
        if item['id_libro'] == id_libro:
            libros[idx] = libro.to_dict()
            break
    save_data(LIBROS_FILE, libros)

def eliminar_libro(id_libro: int):
    libros = load_data(LIBROS_FILE)
    libros = [libro for libro in libros if libro['id_libro'] != id_libro]
    save_data(LIBROS_FILE, libros)

def buscar_libro(criterio: str, valor: str):
    libros = load_data(LIBROS_FILE)
    return [Libro.from_dict(libro) for libro in libros if libro[criterio] == valor]

# Gestión de socios
def registrar_socio(socio: Socio):
    socios = load_data(SOCIOS_FILE)
    socio.id_socio = get_next_id(socios)
    socios.append(socio.to_dict())
    save_data(SOCIOS_FILE, socios)

def editar_socio(id_socio: int, socio: Socio):
    socios = load_data(SOCIOS_FILE)
    for idx, item in enumerate(socios):
        if item['id_socio'] == id_socio:
            socios[idx] = socio.to_dict()
            break
    save_data(SOCIOS_FILE, socios)

def eliminar_socio(id_socio: int):
    socios = load_data(SOCIOS_FILE)
    socios = [socio for socio in socios if socio['id_socio'] != id_socio]
    save_data(SOCIOS_FILE, socios)

# Gestión de préstamos
def registrar_prestamo(prestamo: Prestamo):
    prestamos = load_data(PRESTAMOS_FILE)
    prestamo.id_prestamo = get_next_id(prestamos)
    prestamos.append(prestamo.to_dict())
    save_data(PRESTAMOS_FILE, prestamos)

def editar_prestamo(id_prestamo: int, prestamo: Prestamo):
    prestamos = load_data(PRESTAMOS_FILE)
    for idx, item in enumerate(prestamos):
        if item['id_prestamo'] == id_prestamo:
            prestamos[idx] = prestamo.to_dict()
            break
    save_data(PRESTAMOS_FILE, prestamos)

def devolver_libro(id_prestamo: int):
    prestamos = load_data(PRESTAMOS_FILE)
    for idx, item in enumerate(prestamos):
        if item['id_prestamo'] == id_prestamo:
            prestamos[idx]['estado_prestamo'] = 'Devuelto'
            break
    save_data(PRESTAMOS_FILE, prestamos)

def generar_reporte(tipo: str, valor: str):
    prestamos = load_data(PRESTAMOS_FILE)
    return [Prestamo.from_dict(prestamo) for prestamo in prestamos if prestamo[tipo] == valor]

