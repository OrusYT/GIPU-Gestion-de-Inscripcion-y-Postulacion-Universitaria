from utils.tkinter import ventana_default, bloqueo_pantalla_completa_default
from utils.tkinter import PhotoImage, messagebox, ttk
from utils.tkinter import *
from views.Iniciar_Sesion import inicio_sesion
from views.Registrarse import registrarse
import os

class menu_inicio(ventana_default, bloqueo_pantalla_completa_default):
    """
    Ventana principal del sistema, hereda de ventana_default.
    """
    def __init__(self):
        super().__init__(titulo="GIPU - Gestión de Inscripción y Postulación Universitaria", ancho=900, alto=600)
        self.logo = None
        self._crear_contenido()

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
        ttk.Label(titulo_frame, text="GIPU", font=("Arial", 18, "bold"), foreground="#2a4f80").pack(anchor="w")
        ttk.Label(titulo_frame, text="Gestión de Inscripción y Postulación Universitaria", font=("Arial", 11), foreground="#2a4f80").pack(anchor="w")

        # Botones de acción (Registrarse / Iniciar Sesión)
        botones_frame = ttk.Frame(header)
        botones_frame.pack(side="right", padx=10)
        ttk.Button(botones_frame, text="Registrarse", width=15, command=self._registrarse).pack(side="left", padx=5)
        ttk.Button(botones_frame, text="Iniciar Sesión", width=15, command=self._iniciar_sesion).pack(side="left", padx=5)

        # ─────────────────────────────
        # CUERPO PRINCIPAL
        # ─────────────────────────────
        contenido = ttk.Frame(frame, padding=(30, 40))
        contenido.pack(expand=True, fill="both")

        # Sección de bienvenida
        ttk.Label(contenido, text="Bienvenido!!", font=("Arial", 14, "bold")).pack(anchor="w", pady=(10, 5))
        ttk.Label(
            contenido,
            text=("Te damos la bienvenida al sistema de Gestión de Inscripción y Postulación Universitaria.\n"
                  "Ingresa en nuestro sitio para que puedas hacer tus respectivos pasos\n"
                  "para sostener tu cupo universitario."),
            font=("Arial", 11), justify="left", wraplength=700
        ).pack(anchor="w", pady=(0, 30))

        # Sección de “Acerca de”
        ttk.Label(contenido, text="Acerca de:", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 5))
        ttk.Label(
            contenido,
            text=("Este sistema tiene como fin ayudar a las universidades a gestionar de manera eficiente\n"
                  "sus inscripciones y postulaciones de manera correcta."),
            font=("Arial", 11), justify="left", wraplength=700
        ).pack(anchor="w", pady=(0, 20))

    # ─────────────────────────────
    # MÉTODOS DE ACCIÓN
    # ─────────────────────────────
    def _registrarse(self):
        registrarse(self)

    def _iniciar_sesion(self):
        inicio_sesion(self)