from utils.tkinter import ventana_modal, bloqueo_pantalla_completa_modal, abrir_derecha_modal
from utils.tkinter import PhotoImage, messagebox, ttk
from utils.tkinter import *
from views.admin.Admin_menu import adminVentana
import json
import os

class inicio_sesion (ventana_modal, bloqueo_pantalla_completa_modal, abrir_derecha_modal):
    """
    Ventana principal de Inicio de sesion, hereda de modelo_modal.
    """
    def __init__(self, master=None, iconos=None):
        super().__init__(titulo="GIPU - Iniciar Sesion", ancho=400, alto=550, master=master, iconos= iconos)
        self.logo = None
        self.master_window = master
        self._crear_contenido()
        self.after(100, self._posicionar_a_derecha)
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
        encabezado.pack(fill="x", pady=10)

        # ─────────────────────────────
        # CUERPO PRINCIPAL
        # ─────────────────────────────
        cuerpo = ttk.Frame(frame)
        cuerpo.pack(fill="y", pady=10)

        # ─────────────────────────────
        # FINAL
        # ─────────────────────────────
        final = ttk.Frame(frame)
        final.pack(fill="x", pady=10)

        # Cargar logo
        logo_path = os.path.join("assets", "img", "Logo_GIPU.png")
        if os.path.exists(logo_path):
            self.logo = PhotoImage(file=logo_path)
            self.logo = self.logo.subsample(4, 4)
            logo_label = ttk.Label(encabezado, image=self.logo)
        logo_label.pack(side="top", padx=(15, 15))

        # Título del sistema
        titulo_frame = ttk.Frame(encabezado)
        titulo_frame.pack(side="top", anchor="center", pady=10)
        #ttk.Label(titulo_frame, text="GIPU", font=("Arial", 32, "bold")).pack(anchor="center")
        ttk.Label(titulo_frame, text="Iniciar Sesión", font=("Arial", 22, "bold"), foreground="#2a4f80").pack(anchor="center")
        registro = ttk.Label(titulo_frame, text="<Registrarse>", font=("Arial", 16, "bold", "underline"), foreground="#2a4f80")
        registro.pack(anchor="center")
        registro.bind("<Button-1>", self._registrarse)

        # Entradas y etiquetas del sistema
        correo_frame = ttk.Frame(cuerpo)
        correo_frame.pack(side="top", anchor="center", pady= 10)
        ttk.Label(correo_frame, text="Correo electronico: ", font=("Arial", 16)).pack(anchor="w")
        self.correo = ttk.Entry(correo_frame, width=50, font=("Arial", 12))
        self.correo.pack(anchor="w")

        contraseña_frame = ttk.Frame(cuerpo)
        contraseña_frame.pack(side="bottom", anchor="center", pady= 10)
        ttk.Label(contraseña_frame, text="Contraseña: ", font=("Arial", 16)).pack(anchor="w")
        self.contraseña = ttk.Entry(contraseña_frame, width=50, font=("Arial", 12), show="*")
        self.contraseña.pack(anchor="w")

        self.recuperar_contra = ttk.Label(contraseña_frame, text="Recuperar Contraseña", font=("Arial", 11), foreground= "Blue", cursor="hand2")
        self.recuperar_contra.pack(side="left", anchor="w", pady=(5,0))
        self.recuperar_contra.bind("<Button-1>", self._recuperar_contraseña)
        self.mostrar_contra= ttk.Label(contraseña_frame, text="Mostrar Contraseña", font=("Arial", 11), foreground= "Blue", cursor="hand2")
        self.mostrar_contra.pack(side="right", anchor="e", pady=(5,0))
        self.mostrar_contra.bind("<Button-1>", self._mostrar_contraseña)

        # Botones de acción
        botones_frame = ttk.Frame(final)
        botones_frame.pack(side="bottom",anchor="s", padx=10)
        ttk.Button(botones_frame, text="Cancelar", width=15, command= self.destroy).pack(side="left", padx=5)
        ttk.Button(botones_frame, text="Aceptar", width=15, command= self._aceptar).pack(side="left", padx=5)

    def _registrarse(self, event=None):
        from views.Registrarse import registrarse
        registrarse(self.master)
        self.destroy()

    def _recuperar_contraseña(self, event=None):
        messagebox.showinfo("Rcuperar contraseña", "Aquí se abrirá la ventana de recuperación de contraseña")

    def _mostrar_contraseña(self, event=None):
        if self.contraseña.cget("show") == "":
            self.contraseña.config(show="*")
            self.mostrar_contra.config(text="Mostrar Contraseña")
        else:
            self.contraseña.config(show="")
            self.mostrar_contra.config(text="Ocultar Contraseña")

    def _aceptar(self, event=None):
        correo_ingresado = self.correo.get().strip()
        contraseña_ingresada = self.contraseña.get().strip()
        if not correo_ingresado or not contraseña_ingresada:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return
        usuario_encontrado = False

        try:
            with open("data/admin.json", "r", encoding='utf-8') as archivo:
                for linea in archivo:
                    try:
                        usuario = json.loads(linea)
                        if usuario["Email"] == correo_ingresado.lower() and usuario["Contraseña"] == contraseña_ingresada:
                            messagebox.showinfo("Inicio de sesión exitoso", f"¡Bienvenido, {usuario['Nombre']} {usuario['Apellido']}!")
                            self.destroy()
                            if self.master_window:
                                self.master_window.destroy()
                            adminVentana()
                            usuario_encontrado = True
                            return
                    except json.JSONDecodeError:
                        continue
        except FileNotFoundError:
            pass

        if not usuario_encontrado:
            try:
                with open("data/datos_registro.json", "r", encoding='utf-8') as archivo:
                    for linea in archivo:
                        try:
                            usuario = json.loads(linea)
                            if usuario["Email"] == correo_ingresado.lower() and usuario["Contraseña"] == contraseña_ingresada:
                                messagebox.showinfo("Inicio de sesión exitoso", f"¡Bienvenido, {usuario['Nombre']} {usuario['Apellido']}!")
                                self.destroy()
                                if self.master_window:
                                    self.master_window.destroy()
                                
                                usuario_encontrado = True
                                return
                        except json.JSONDecodeError:
                            continue
            except FileNotFoundError:
                pass
        if not usuario_encontrado:
            messagebox.showerror("Error de autenticación", "Correo o contraseña incorrectos.")