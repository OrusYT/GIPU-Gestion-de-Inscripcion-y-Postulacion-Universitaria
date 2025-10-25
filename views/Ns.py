from utils.tkinter import ventana_default, bloqueo_pantalla_completa_default, ventana_modal
import tkinter as tk

class miVentana(ventana_default,bloqueo_pantalla_completa_default,ventana_modal):

    def configurar(self):
        self.config(bg="lightblue")
        self.geometry(f"{self.ancho}x{self.alto}+100+100")

        # Texto principal
        texto = tk.Label(self, text="¡Bienvenido a tu ventana personalizada!", font=("Arial", 16), bg="lightblue")
        texto.pack(pady=20)

    def abrir_modal(self):
        ventana_modal(self, titulo="Modal de prueba", mensaje="Este es un mensaje dentro de la ventana modal.")

