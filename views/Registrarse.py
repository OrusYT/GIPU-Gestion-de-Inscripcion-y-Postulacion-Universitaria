from utils.tkinter import ventana_modal, bloqueo_pantalla_completa_modal
from utils.tkinter import PhotoImage, messagebox, ttk
from utils.tkinter import *
from views.Iniciar_Sesion import inicio_sesion
import json
import os

class registrarse (ventana_modal, bloqueo_pantalla_completa_modal):
    def __init__(self, master=None, iconos=None):
        super().__init__(titulo="GIPU - Registrarse", ancho=600, alto=750, master=master, iconos= iconos)
        self.logo = None
        self._crear_contenido()
        self.transient(master)
        self.grab_set()
        self.focus_set()

    def _crear_contenido(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(expand=True, fill="both")

        # ─────────────────────────────
        # ENCABEZADO
        # ─────────────────────────────
        encabezado = ttk.Frame(frame)
        encabezado.pack(fill="x", pady=(10,0.5))

        # ─────────────────────────────
        # CUERPO PRINCIPAL
        # ─────────────────────────────
        cuerpo_contenedor = ttk.Frame(frame)
        cuerpo_contenedor.pack(expand=True, fill="both", pady=10)

        cuerpo_centro = ttk.Frame(cuerpo_contenedor)
        cuerpo_centro.pack(expand=True)

        cuerpo_d = ttk.Frame(cuerpo_centro)
        cuerpo_d.pack(fill="y", pady=5, padx=15, side="right")
        cuerpo_i = ttk.Frame(cuerpo_centro)
        cuerpo_i.pack(fill="y", pady=5, padx=15, side="left")

        # ─────────────────────────────
        # FINAL
        # ─────────────────────────────
        final = ttk.Frame(frame)
        final.pack(fill="x", pady=(20,10), side="bottom")

        # Cargar logo
        logo_path = os.path.join("assets", "img", "Logo_GIPU.png")
        if os.path.exists(logo_path):
            self.logo = PhotoImage(file=logo_path)
            self.logo = self.logo.subsample(6, 6)
            logo_label = ttk.Label(encabezado, image=self.logo)
        logo_label.pack(side="top", padx=(15, 15))

        # Título del sistema
        titulo_frame = ttk.Frame(encabezado)
        titulo_frame.pack(side="top", anchor="center", pady=10)
        ttk.Label(titulo_frame, text="Registrarse", font=("Arial", 22, "bold"), foreground="#2a4f80").pack(anchor="center")
        sesion = ttk.Label(titulo_frame, text="<Iniciar Sesión>", font=("Arial", 15, "bold", "underline"), foreground="#2a4f80")
        sesion.pack(anchor="center")
        sesion.bind("<Button-1>", self._iniciar_sesion)

        # Entradas y etiquetas del sistema
        nombre_frame = ttk.Frame(cuerpo_i)
        nombre_frame.pack(side="top", anchor="center", pady= 10)
        ttk.Label(nombre_frame, text="Nombre: ", font=("Arial", 16)).pack(anchor="w")
        self.nombre = ttk.Entry(nombre_frame, width=25, font=("Arial", 12))
        self.nombre.pack(anchor="w")

        apellido_frame = ttk.Frame(cuerpo_i)
        apellido_frame.pack(side="top", anchor="center", pady= 10)
        ttk.Label(apellido_frame, text="Apellido: ", font=("Arial", 16)).pack(anchor="w")
        self.apellido = ttk.Entry(apellido_frame, width=25, font=("Arial", 12))
        self.apellido.pack(anchor="w")

        ci_frame = ttk.Frame(cuerpo_i)
        ci_frame.pack(side="top", anchor="center", pady= 10)
        ttk.Label(ci_frame, text="C.I.: ", font=("Arial", 16)).pack(anchor="w")
        self.ci = ttk.Entry(ci_frame, width=25, font=("Arial", 12))
        self.ci.pack(anchor="w")

        email_frame = ttk.Frame(cuerpo_i)
        email_frame.pack(side="top", anchor="center", pady= 10)
        ttk.Label(email_frame, text="Email: ", font=("Arial", 16)).pack(anchor="w")
        self.email = ttk.Entry(email_frame, width=25, font=("Arial", 12))
        self.email.pack(anchor="w")

        # Contraseña ──────────────────────────────────────────────────────────
        contraseña_frame = ttk.Frame(cuerpo_i)
        contraseña_frame.pack(side="top", anchor="center", pady= 10)
        ttk.Label(contraseña_frame, text="Contraseña: ", font=("Arial", 16)).pack(anchor="w")
        self.contraseña = ttk.Entry(contraseña_frame, width=25, font=("Arial", 12), show="*")
        self.contraseña.pack(anchor="w")

        self.mostrar_contra= ttk.Label(contraseña_frame, text="Mostrar Contraseña", font=("Arial", 11), foreground= "Blue", cursor="hand2")
        self.mostrar_contra.pack(side="right", anchor="e", pady=(5,0))
        self.mostrar_contra.bind("<Button-1>", self._mostrar_contraseña)
        # ──────────────────────────────────────────────────────────────────────

        direccion_frame = ttk.Frame(cuerpo_d)
        direccion_frame.pack(side="top", anchor="center", pady= 10)
        ttk.Label(direccion_frame, text="Dirección: ", font=("Arial", 16)).pack(anchor="w")
        self.direccion = ttk.Entry(direccion_frame, width=25, font=("Arial", 12))
        self.direccion.pack(anchor="w")

        telefono_frame = ttk.Frame(cuerpo_d)
        telefono_frame.pack(side="top", anchor="center", pady= 10)
        ttk.Label(telefono_frame, text="Teléfono: ", font=("Arial", 16)).pack(anchor="w")
        self.telefono = ttk.Entry(telefono_frame, width=25, font=("Arial", 12))
        self.telefono.pack(anchor="w")

        genero_frame = ttk.Frame(cuerpo_d)
        genero_frame.pack(side="top", anchor="center", pady= 10)
        ttk.Label(genero_frame, text="Género: ", font=("Arial", 16)).pack(anchor="w")
        self.genero = ttk.Combobox(genero_frame, width=23, font=("Arial", 12))
        self.genero["values"] = ("","Masculino", "Femenino", "Prefiero no decirlo")
        self.genero.current(0)
        self.genero.pack(anchor="w")

        # Contraseña repetida ──────────────────────────────────────────────────
        repetir_contraseña_frame = ttk.Frame(cuerpo_d)
        repetir_contraseña_frame.pack(side="top", anchor="center", pady= 10)
        ttk.Label(repetir_contraseña_frame, text="Repetir Contraseña: ", font=("Arial", 16)).pack(anchor="w")
        self.repetir_contraseña = ttk.Entry(repetir_contraseña_frame, width=25, font=("Arial", 12), show="*")
        self.repetir_contraseña.pack(anchor="w")

        self.mostrar_contra_repetir= ttk.Label(repetir_contraseña_frame, text="Mostrar Contraseña", font=("Arial", 11), foreground= "Blue", cursor="hand2")
        self.mostrar_contra_repetir.pack(side="right", anchor="e", pady=(5,0))
        self.mostrar_contra_repetir.bind("<Button-1>", self._mostrar_contraseña_repetida)
        # ──────────────────────────────────────────────────────────────────────

        # Botones de acción
        botones_frame = ttk.Frame(final)
        botones_frame.pack(side="top",anchor="center", padx=10)
        ttk.Button(botones_frame, text="Cancelar", width=15, command= self.destroy).pack(side="left", padx=5,pady=0.01)
        ttk.Button(botones_frame, text="Aceptar", width=15, command= self._aceptar).pack(side="left", padx=5,pady=0.01)

    def _iniciar_sesion(self, event=None):
        from views.Iniciar_Sesion import inicio_sesion
        inicio_sesion(self.master)
        self.destroy()
    
    def _mostrar_contraseña(self, event=None):
        if self.contraseña.cget("show") == "":
            self.contraseña.config(show="*")
            self.mostrar_contra.config(text="Mostrar Contraseña")
        else:
            self.contraseña.config(show="")
            self.mostrar_contra.config(text="Ocultar Contraseña")

    def _mostrar_contraseña_repetida(self, event=None):
        if self.repetir_contraseña.cget("show") == "":
            self.repetir_contraseña.config(show="*")
            self.mostrar_contra_repetir.config(text="Mostrar Contraseña")
        else:
            self.repetir_contraseña.config(show="")
            self.mostrar_contra_repetir.config(text="Ocultar Contraseña")

    def guardar_datos(self):
        datos = {
            "Email": self.email.get(),
            "Contraseña": self.contraseña.get(),
            "Nombre": self.nombre.get(),
            "Apellido": self.apellido.get(),
            "C.I.": self.ci.get(),
            "Dirección": self.direccion.get(),
            "Teléfono": self.telefono.get(),
            "Género": self.genero.get()
        }

        with open("data/datos_registro.json", "a", encoding='utf-8') as archivo:
            archivo.write(json.dumps(datos) + "\n")

    def _aceptar(self):
        campos={
            "Nombre":self.nombre.get(),
            "Apellido":self.apellido.get(),
            "C.I":self.ci.get(),
            "Email":self.email.get(),
            "Contraseña":self.contraseña.get(),
            "Direccion":self.direccion.get(),
            "Telefono":self.telefono.get(),
            "Genero":self.genero.get(),
            "Repetir Contraseña":self.repetir_contraseña.get()
        }
        for campo, valor in campos.items():
            if not valor.strip():
                messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
                return
            if campos["Contraseña"] != campos["Repetir Contraseña"]:
                messagebox.showwarning("Contraseñas no coinciden", "Las contraseñas ingresadas no coinciden. Por favor, inténtelo de nuevo.")
                return
        self.guardar_datos()
        messagebox.showinfo("Registro exitoso", "¡Te has registrado correctamente!")
        inicio_sesion(self)
        self.destroy()
