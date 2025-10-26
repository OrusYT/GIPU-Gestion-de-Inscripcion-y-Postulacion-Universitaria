import tkinter as tk
from tkinter import PhotoImage
import os

class Iconos:
    def __init__(self):
        self.icono = "Icono_GIPU_pequeño.ico"
        self.icono_grande = "Icono_GIPU_grande.ico"
        self.icono_png = "Icono_GIPU.png"

    def cargar(self, ventana, icono=None, icono_grande=None):
        """
        Carga los iconos en una ventana específica
        """
        if icono is None:
            icono = self.icono
        if icono_grande is None:
            icono_grande = self.icono_grande
        
        try:
            # Método 1: Cargar el icono ICO pequeño
            icono_path = os.path.join("assets", "iconos", icono)
            if os.path.exists(icono_path):
                ventana.iconbitmap(icono_path)
            
            # Método 2: Cargar el icono ICO grande
            icono_grande_path = os.path.join("assets", "iconos", icono_grande)
            if os.path.exists(icono_grande_path):
                ventana.iconbitmap(icono_grande_path)
                
            # Método 1: Cargar el icono PNG
            icono_png_path = os.path.join("assets", "iconos", self.icono_png)
            if os.path.exists(icono_png_path):
                try:
                    img = PhotoImage(file=icono_png_path)
                    ventana.iconphoto(True, img)  # True = icono por defecto
                    # Guardar referencia para evitar garbage collection
                    if not hasattr(ventana, '_icons'):
                        ventana._icons = []
                    ventana._icons.append(img)
                except Exception as e:
                    print(f"No se pudo cargar icono PNG: {e}")
        except Exception as e:
            print(f"Error estableciendo icono de barra de tareas: {e}")

    def obtener(self):
        return self.icono, self.icono_grande