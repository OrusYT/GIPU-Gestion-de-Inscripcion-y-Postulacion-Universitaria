from utils.tkinter import ventana_default, bloqueo_pantalla_completa_default, ventana_modal
from utils.tkinter import PhotoImage, messagebox, ttk
from utils.tkinter import *
import tkinter as tk
from abc import ABCMeta, abstractmethod
import os, json

class estudianteventana(ventana_default):
    def __init__(self, master=None, iconos=None):
        super().__init__(titulo="GIPU - Bienvenido ", ancho=800, alto=600, iconos= iconos)
        self.logo = None
        self.inicio()
        
    def inicio(self):
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
            try:
                self.logo = tk.PhotoImage(file=logo_path)
                self.logo = self.logo.subsample(7, 7)
                logo_label = ttk.Label(header, image=self.logo)
                logo_label.pack(side="left", padx=(10, 15))
            except Exception as e:
                print("Error cargando imagen:", e)
                ttk.Label(header, text="[Logo]").pack(side="left", padx=(10,15))
        else:
            ttk.Label(header, text="[Logo no encontrado]").pack(side="left", padx=(10,15))


        # Título del sistema
        titulo_frame = ttk.Frame(header)
        titulo_frame.pack(side="left", anchor="center", pady=10)
        ttk.Label(titulo_frame, text="GIPU", font=("Arial", 20, "bold"), foreground="#2a4f80").pack(anchor="w")
        ttk.Label(titulo_frame, text="Bienvenido", font=("Arial", 18), foreground="#2a4f80").pack(anchor="w")
        boton_frame = ttk.Frame(frame)
        boton_frame.pack(side="left", anchor="ne", pady=0, padx=10)
        boton1 = tk.Button(boton_frame, text="Verificar registro unico", font=("Arial", 12), command=self.abrir_modal)
        boton1.pack(side="left", padx=5)
        boton2 = tk.Button(boton_frame, text="Añadir postulacion", font=("Arial", 12), command=self.abrir_modal)
        boton2.pack(side="left", padx=5)
        boton3 = tk.Button(boton_frame, text="Salir", font=("Arial", 12), command=self.abrir_modal)
        boton3.pack(side="left", padx=5)
        

    def abrir_modal(self):
        herramienta_modal(self)
class herramienta_modal(ventana_modal,bloqueo_pantalla_completa_default):

    def __init__(self, master=None):
        super().__init__(master)
        self.agregar_postulacion
        self.verificar_registrounico()
        self.salir()

