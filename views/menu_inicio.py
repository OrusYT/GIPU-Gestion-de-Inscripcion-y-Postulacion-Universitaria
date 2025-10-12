from utils.tkinter import ventana_default
from tkinter import ttk, messagebox

class menu_inicio(ventana_default):
    """
    Ventana principal del sistema, hereda de VentanaDefault.
    """
    def __init__(self):
        super().__init__(titulo="Menú de Inicio", ancho=700, alto=500)
        self._crear_widgets()

    def _crear_widgets(self):
        frame = ttk.Frame(self, padding=20)
        frame.pack(expand=True)

        ttk.Label(frame, text="Bienvenido al Sistema de Inscripción y Postulación",
                  font=("Arial", 14, "bold")).pack(pady=20)
        
        ttk.Button(frame, text="Registrarse", command=self._accion_postular).pack(pady=10)
        ttk.Button(frame, text="Iniciar Sesion", command=self._accion_postular).pack(pady=10)

    def _accion_postular(self):
        messagebox.showinfo("Registro", "Aquí se abrirá la ventana de regitro de cuentas")
        #registro = ventana_registro()
        #registro.run()

    def _accion_convocatorias(self):
        messagebox.showinfo("CIniciar Sesion", "Aquí se mostrara la ventana de Inicio de sesion.")
        #inicio_sesion = ventana_inicio()
        #inicio_sesion.run()