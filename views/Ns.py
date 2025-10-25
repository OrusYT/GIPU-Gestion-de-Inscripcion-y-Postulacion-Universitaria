from utils.tkinter import ventana_default, bloqueo_pantalla_completa_default, ventana_modal
from utils.tkinter import PhotoImage, messagebox, ttk
from utils.tkinter import *
import tkinter as tk

class adminVentana(ventana_default, bloqueo_pantalla_completa_default, ventana_modal):
    def configurar(self):
        self.config(bg="#f0f0f0") 
        self.geometry(f"{self.ancho}x{self.alto}+50+50") 

     
        titulo = tk.Label(self, text="Panel de Administración", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#2a4f80")
        titulo.pack(pady=30)

      
        texto = tk.Label(self, text="Bienvenido, administrador. Aquí puedes gestionar usuarios y configuraciones.",
                         font=("Arial", 14), bg="#f0f0f0")
        texto.pack(pady=10)


        boton = tk.Button(self, text="Abrir herramientas", font=("Arial", 12), command=self.abrir_modal)
        boton.pack(pady=20)

    def abrir_modal(self):
        ventana_modal(self, titulo="Herramientas de Admin", mensaje="Aquí irían las funciones administrativas.")