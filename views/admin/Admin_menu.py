from utils.tkinter import ventana_default, bloqueo_pantalla_completa_default, ventana_modal
from utils.tkinter import PhotoImage, messagebox, ttk
from utils.tkinter import *
import tkinter as tk
from abc import ABCMeta, abstractmethod
import os, json

class adminVentana(ventana_default, bloqueo_pantalla_completa_default,ventana_modal):
    def __init__(self, master=None, iconos=None):
        super().__init__(titulo="GIPU - Panel de Administración", ancho=800, alto=600, iconos= iconos)
        self.logo = None
        self._crear_contenido()
        self.abrir_modal()
    def _crear_contenido(self):
        # Frame principal
        frame = ttk.Frame(self, padding=30)
        frame.pack(expand=True, fill="both")
        # ─────────────────────────────
        # ENCABEZADO
        # ─────────────────────────────
        header = ttk.Frame(frame)
        header.pack(fill="x", pady=10)
        # Cargar logo
        logo_path = os.path.join("assets", "img", "Logo_GIPU.png")
        if os.path.exists(logo_path):
            self.logo = PhotoImage(file=logo_path)
            self.logo = self.logo.subsample(7, 7)
            logo_label = ttk.Label(header, image=self.logo)
        logo_label.pack(side="left", padx=(10, 15))
        # Título del sistema
        titulo_frame = ttk.Frame(header)
        titulo_frame.pack(side="left", anchor="center", pady=10)
        ttk.Label(titulo_frame, text="GIPU", font=("Arial", 20, "bold"), foreground="#2a4f80").pack(anchor="w")
        ttk.Label(titulo_frame, text="Panel de Administracion", font=("Arial", 18), foreground="#2a4f80").pack(anchor="w")
        boton = tk.Button(frame, text="Abrir herramientas", font=("Arial", 12), command=self.abrir_modal)
        boton.pack(pady=20)
    def abrir_modal(self):
        herramienta_modal(self)
    
class herramienta_modal(ventana_modal,bloqueo_pantalla_completa_default):
    def __init__(self, master=None):
        super().__init__(titulo="Herramientas de Administración", ancho=400, alto=300, master=master)
        
        self._crear_contenido()
    def _crear_contenido(self):
        self.admin_menu = Admin_menu()
        self.frame = ttk.Frame(self, padding=10)
        self.frame.pack(expand=True, fill="both")
        titulo = tk.Label(self.frame, text="Herramientas de Administración", font=("Arial", 16, "bold"))
        titulo.pack(pady=20)
        inscripcionboton=tk.Button(self.frame, text="Gestionar Inscripciones", command=self.admin_menu.Gestionar_inscripciones)
        inscripcionboton.pack(pady=10)
        cerrar_boton = tk.Button(self.frame, text="Cerrar", command=self.destroy)
        cerrar_boton.pack(pady=20)


class Admin_menu:
    #Idea esto se usara para cuando se inicie por primera vez el administrador tendra que colocar la universidad

    def Gestionar_inscripciones(self):
        messagebox.showinfo("Gestionar Inscripciones", "Funcionalidad en desarrollo.")

    def Gestionar_postulaciones(self):
        print("Gestionar postulaciones")
        print("Periodo(ya se puso en las inscripciones): ")
        print("modificar porcentaje de abanderados: ")
        print()
    
    def Gestionar_usuarios(self):
        print("Gestionar usuarios")
        print("Buscar: ")
        print("Suspender cuenta: ")
        print("Eliminar cuenta: ")
        print("Modificar cuenta: ")
        print()
    
    def Gestionar_administradores(self):
        print("Gestionar administradores")
        print("Buscar: ")
        print("Crear administrador: ")
        print("Suspender cuenta: ")
        print("Eliminar cuenta: ")
        print("Modificar cuenta: ")
        print()
    def _contenedor_oferta(self):
        pass

