from utils.tkinter import ventana_default, bloqueo_pantalla_completa_default, ventana_modal
from utils.tkinter import PhotoImage, messagebox, ttk
from utils.tkinter import *
import tkinter as tk

class adminVentana(ventana_default, bloqueo_pantalla_completa_default, ventana_modal):
    def __init__(self, master=None):
        super().__init__(titulo="GIPU - Panel de Administración", ancho=800, alto=600)
        self.configurar()
        self._crear_contenido()
        self.master = master
    def configurar(self):

        if hasattr(self, "ancho") and hasattr(self, "alto"):
            self.geometry(f"{self.ancho}x{self.alto}+50+50")
        else:
            self.geometry("800x600+50+50")

    def _crear_contenido(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(expand=True, fill="both")
        titulo = tk.Label(frame, text="Panel de Administración", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#2a4f80")
        titulo.pack(pady=30,anchor="center")

        boton = tk.Button(frame, text="Abrir herramientas", font=("Arial", 12), command=self.abrir_modal)
        boton.pack(pady=20)
    def abrir_modal(self):
        herramienta_modal(self)
    
class herramienta_modal(ventana_modal,bloqueo_pantalla_completa_default):
    def __init__(self, master=None):
        super().__init__(titulo="Herramientas de Administración", ancho=400, alto=300, master=master)
        self._crear_contenido()
    def _crear_contenido(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(expand=True, fill="both")
        titulo = tk.Label(frame, text="Herramientas de Administración", font=("Arial", 16, "bold"))
        titulo.pack(pady=20)
        texto = tk.Label(frame, text="Aquí puedes agregar herramientas administrativas adicionales.", font=("Arial", 12))
        texto.pack(pady=10)
        cerrar_boton = tk.Button(frame, text="Cerrar", command=self.destroy)
        cerrar_boton.pack(pady=20)