from abc import ABCMeta, abstractmethod
import os, json

class Admin_menu(metaclass=ABCMeta):
    #Idea esto se usara para cuando se inicie por primera vez el administrador tendra que colocar la universidad
    """if not os.path.exists("config\settings.json"):
            Instituto = {
                "Universidad": "Universidad Laica Eloy Alfaro de Manabi"
            }
            with open("settings.json", "w", encoding="utf-8") as archivo:
                json.dump(Instituto, archivo, indent=4)"""
    def Gestionar_inscripciones(self):
        print("Gestionar inscripciones")
        print("Ingrese un periodo: ")
        print("Oferta academica: ")
        print()
    
    def Gestionar_postulaciones(self):
        print("Gestionar postulaciones")
        print("Periodo(ya se puso en las inscripciones): ")
        print("modificar porcentaje de abanderados: ")
        print()
    
    def Gestionar_usuarios(self):
        print("Gestionar usuarios")
        print("Buscar: ")
        print("Suspender cuenta: ")
        print("Eliminar cuenta: ")
        print("Modificar cuenta: ")
        print()
    
    def Gestionar_administradores(self):
        print("Gestionar administradores")
        print("Buscar: ")
        print("Crear administrador: ")
        print("Suspender cuenta: ")
        print("Eliminar cuenta: ")
        print("Modificar cuenta: ")
        print()

menu = Admin_menu()
menu.Gestionar_inscripciones()
menu.Gestionar_postulaciones()
menu.Gestionar_usuarios()
menu.Gestionar_administradores()