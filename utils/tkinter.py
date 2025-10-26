import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from tkinter import *

class ventana_default(tk.Tk):
    # Se crea la clase de la ventana default, hereda de Tkinter.
    def __init__(self, titulo="Sistema de Inscripción y Postulación", ancho=800, alto=600, iconos=None):
        super().__init__()
        self.title(titulo)

        # Dimensiones centradas en pantalla
        self.ancho = ancho
        self.alto = alto
        self._centrar_ventana()

        # Fondo y estilos generales
        self.config(bg="#f0f0f0")
        self._configurar_estilos()

        #iconos
        if iconos:
            iconos.cargar(self)


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
    

class bloqueo_pantalla_completa_default(tk.Tk):
    # Bloqueo de fullscream
    def __init__(self):
        super().__init__()
        self.bloquear_pantalla_completa()

    def bloquear_pantalla_completa(self):     
        self.attributes("-fullscreen", False)
        self.attributes("-topmost", False)
        self.resizable(False, False)

class ventana_modal(tk.Toplevel):
    def __init__(self, titulo="modelo", ancho=800, alto=600, master=None, iconos=None):
        super().__init__(master)
        self.title(titulo)

        # Dimensiones centradas en pantalla
        self.ancho = ancho
        self.alto = alto
        self._centrar_ventana()

        # Fondo y estilos generales
        self.config(bg="#f0f0f0")
        self._configurar_estilos()
    
        #iconos
        if iconos:
            iconos.cargar(self)

    def _centrar_ventana(self):
        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()
        x = (pantalla_ancho - self.ancho) // 2
        y = (pantalla_alto - self.alto) // 2
        self.geometry(f"{self.ancho}x{self.alto}+{x}+{y}")

    def _configurar_estilos(self):
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("TButton", font=("Arial", 11), padding=5, background="#cca14c")
        estilo.configure("TLabel", font=("Arial", 11), background = "#ffffff")
        estilo.configure("TFrame", background="#ffffff")

    def run(self):
        """Inicia el loop principal."""
        self.mainloop()

class bloqueo_pantalla_completa_modal(tk.Toplevel):
    # Bloqueo de fullscream
    def __init__(self, master=None):
        super().__init__(master)
        self.bloquear_pantalla_completa()

    def bloquear_pantalla_completa(self):     
        self.attributes("-fullscreen", False)
        self.attributes("-topmost", False)
        self.resizable(False, False)

class abrir_derecha_modal(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self._posicionar_a_derecha()
    
    def _posicionar_a_derecha(self):
        if self.master:
            self.master.update_idletasks()
            master_x = self.master.winfo_x()
            master_y = self.master.winfo_y()
            master_w = self.master.winfo_width()
            master_h = self.master.winfo_height()

            # Dimensiones propias
            self.update_idletasks()
            w = self.winfo_width()
            h = self.winfo_height()

            # Calcular posición a la derecha
            x = master_x + master_w
            y = master_y

            # Mostrar en la posición calculada
            self.geometry(f"{w}x{h}+{x+10}+{y+25}")