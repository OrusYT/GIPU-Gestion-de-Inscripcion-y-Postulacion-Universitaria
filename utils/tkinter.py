import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from tkinter import *

class ventana_default(tk.Tk):
    # Se crea la clase de la ventana default, hereda de Tkinter.
    def __init__(self, titulo="Sistema de Inscripción y Postulación", ancho=800, alto=600):
        super().__init__()
        self.title(titulo)

        # Dimensiones centradas en pantalla
        self.ancho = ancho
        self.alto = alto
        self._centrar_ventana()

        # Fondo y estilos generales
        self.config(bg="#f0f0f0")
        self._configurar_estilos()

    # ─────────────────────────────
    # Posicionar ventana
    # ─────────────────────────────
    def _centrar_ventana(self):
        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()
        x = (pantalla_ancho - self.ancho) // 2
        y = (pantalla_alto - self.alto) // 2
        self.geometry(f"{self.ancho}x{self.alto}+{x}+{y}")

    # ─────────────────────────────
    # Configuracion de estilos base
    # ─────────────────────────────
    def _configurar_estilos(self):
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("TButton", font=("Arial", 11), padding=5, background="#cca14c")
        estilo.configure("TLabel", font=("Arial", 11), background = "#ffffff")
        estilo.configure("TFrame", background="#ffffff")

    # ─────────────────────────────
    # Abrir la ventana
    # ─────────────────────────────
    def run(self):
        """Inicia el loop principal."""
        self.mainloop()
    

class bloqueo_pantalla_completa(tk.Tk):
    # Bloqueo de fullscream
    def __init__(self):
        super().__init__()
        self.bloqueo_pantalla_completa()

    def bloqueo_pantalla_completa(self):     
        self.attributes("-fullscreen", False)
        self.attributes("-topmost", False)
        self.resizable(False, False)