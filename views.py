
# views.py
import tkinter as tk
from tkinter import messagebox, ttk
from controllers import (
    registrar_libro, editar_libro, eliminar_libro, buscar_libro,
    registrar_socio, editar_socio, eliminar_socio,
    registrar_prestamo, editar_prestamo, devolver_libro, generar_reporte
)
from models import Libro, Socio, Prestamo

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Bibliotecas")
        self.create_widgets()

    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=1, fill="both")

        tab_libros = ttk.Frame(tab_control)
        tab_control.add(tab_libros, text='Libros')
        self.create_libro_widgets(tab_libros)

        tab_socios = ttk.Frame(tab_control)
        tab_control.add(tab_socios, text='Socios')
        self.create_socio_widgets(tab_socios)

        tab_prestamos = ttk.Frame(tab_control)
        tab_control.add(tab_prestamos, text='Préstamos')
        self.create_prestamo_widgets(tab_prestamos)

        tab_busqueda = ttk.Frame(tab_control)
        tab_control.add(tab_busqueda, text='Búsqueda')
        self.create_busqueda_widgets(tab_busqueda)

        tab_reporte = ttk.Frame(tab_control)
        tab_control.add(tab_reporte, text='Reportes')
        self.create_reporte_widgets(tab_reporte)

    def create_libro_widgets(self, frame):
        tk.Label(frame, text="Título:").grid(row=0, column=0, sticky="e")
        self.titulo_entry = tk.Entry(frame)
        self.titulo_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="Autor:").grid(row=1, column=0, sticky="e")
        self.autor_entry = tk.Entry(frame)
        self.autor_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(frame, text="Editorial:").grid(row=2, column=0, sticky="e")
        self.editorial_entry = tk.Entry(frame)
        self.editorial_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(frame, text="Año de Publicación:").grid(row=3, column=0, sticky="e")
        self.anio_entry = tk.Entry(frame)
        self.anio_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(frame, text="Género:").grid(row=4, column=0, sticky="e")
        self.genero_entry = tk.Entry(frame)
        self.genero_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(frame, text="Cantidad Disponible:").grid(row=5, column=0, sticky="e")
        self.cantidad_entry = tk.Entry(frame)
        self.cantidad_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Button(frame, text="Registrar Libro", command=self.registrar_libro).grid(row=6, column=0, columnspan=2, pady=10)

    def registrar_libro(self):
        libro = Libro(
            id_libro=None,
            titulo=self.titulo_entry.get(),
            autor=self.autor_entry.get(),
            editorial=self.editorial_entry.get(),
            anio_publicacion=int(self.anio_entry.get()),
            genero=self.genero_entry.get(),
            cantidad_disponible=int(self.cantidad_entry.get())
        )
        registrar_libro(libro)
        messagebox.showinfo("Éxito", "Libro registrado exitosamente")

    def create_socio_widgets(self, frame):
        tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="e")
        self.nombre_entry = tk.Entry(frame)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="Apellido:").grid(row=1, column=0, sticky="e")
        self.apellido_entry = tk.Entry(frame)
        self.apellido_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(frame, text="Fecha de Nacimiento:").grid(row=2, column=0, sticky="e")
        self.fecha_entry = tk.Entry(frame)
        self.fecha_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(frame, text="Dirección:").grid(row=3, column=0, sticky="e")
        self.direccion_entry = tk.Entry(frame)
        self.direccion_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(frame, text="Correo Electrónico:").grid(row=4, column=0, sticky="e")
        self.correo_entry = tk.Entry(frame)
        self.correo_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(frame, text="Teléfono:").grid(row=5, column=0, sticky="e")
        self.telefono_entry = tk.Entry(frame)
        self.telefono_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Button(frame, text="Registrar Socio", command=self.registrar_socio).grid(row=6, column=0, columnspan=2, pady=10)

    def registrar_socio(self):
        socio = Socio(
            id_socio=None,
            nombre=self.nombre_entry.get(),
            apellido=self.apellido_entry.get(),
            fecha_nacimiento=self.fecha_entry.get(),
            direccion=self.direccion_entry.get(),
            correo_electronico=self.correo_entry.get(),
            telefono=self.telefono_entry.get()
        )
        registrar_socio(socio)
        messagebox.showinfo("Éxito", "Socio registrado exitosamente")

    def create_prestamo_widgets(self, frame):
        tk.Label(frame, text="ID de Socio:").grid(row=0, column=0, sticky="e")
        self.id_socio_entry = tk.Entry(frame)
        self.id_socio_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="ID de Libro:").grid(row=1, column=0, sticky="e")
        self.id_libro_entry = tk.Entry(frame)
        self.id_libro_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(frame, text="Fecha de Préstamo:").grid(row=2, column=0, sticky="e")
        self.fecha_prestamo_entry = tk.Entry(frame)
        self.fecha_prestamo_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(frame, text="Costo:").grid(row=3, column=0, sticky="e")
        self.costo_entry = tk.Entry(frame)
        self.costo_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(frame, text="Fecha de Devolución:").grid(row=4, column=0, sticky="e")
        self.fecha_devolucion_entry = tk.Entry(frame)
        self.fecha_devolucion_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(frame, text="Registrar Préstamo", command=self.registrar_prestamo).grid(row=5, column=0, columnspan=2, pady=10)

    def registrar_prestamo(self):
        prestamo = Prestamo(
            id_prestamo=None,
            id_socio=int(self.id_socio_entry.get()),
            id_libro=int(self.id_libro_entry.get()),
            fecha_prestamo=self.fecha_prestamo_entry.get(),
            costo=float(self.costo_entry.get()),
            fecha_devolucion=self.fecha_devolucion_entry.get(),
            estado_prestamo="En Curso"
        )
        registrar_prestamo(prestamo)
        messagebox.showinfo("Éxito", "Préstamo registrado exitosamente")

    def create_busqueda_widgets(self, frame):
        tk.Label(frame, text="Criterio:").grid(row=0, column=0, sticky="e")
        self.criterio_entry = tk.Entry(frame)
        self.criterio_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="Valor:").grid(row=1, column=0, sticky="e")
        self.valor_entry = tk.Entry(frame)
        self.valor_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(frame, text="Buscar Libro", command=self.buscar_libro).grid(row=2, column=0, columnspan=2, pady=10)

    def buscar_libro(self):
        criterio = self.criterio_entry.get()
        valor = self.valor_entry.get()
        libros = buscar_libro(criterio, valor)
        result = "\n".join([libro.titulo for libro in libros])
        messagebox.showinfo("Resultado de Búsqueda", result)

    def create_reporte_widgets(self, frame):
        tk.Label(frame, text="Tipo:").grid(row=0, column=0, sticky="e")
        self.tipo_entry = tk.Entry(frame)
        self.tipo_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="Valor:").grid(row=1, column=0, sticky="e")
        self.valor_reporte_entry = tk.Entry(frame)
        self.valor_reporte_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(frame, text="Generar Reporte", command=self.generar_reporte).grid(row=2, column=0, columnspan=2, pady=10)

    def generar_reporte(self):
        tipo = self.tipo_entry.get()
        valor = self.valor_reporte_entry.get()
        prestamos = generar_reporte(tipo, valor)
        result = "\n".join([f"Préstamo ID: {prestamo.id_prestamo}, Libro ID: {prestamo.id_libro}, Socio ID: {prestamo.id_socio}" for prestamo in prestamos])
        messagebox.showinfo("Reporte de Préstamos", result)
