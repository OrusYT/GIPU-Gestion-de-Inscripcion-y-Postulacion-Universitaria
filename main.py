from views.menu_inicio import menu_inicio
#from views.Iniciar_Sesion import inicio_sesion
from views.estudiante_menu import estudianteventana
from config.iconos import Iconos

if __name__ == "__main__":
    iconos = Iconos()
    app = menu_inicio(iconos=iconos)
    app.run()
    