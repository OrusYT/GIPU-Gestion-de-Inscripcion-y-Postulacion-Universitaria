#from views.menu_inicio import menu_inicio
#from views.Iniciar_Sesion import inicio_sesion
from views.admin.Admin_menu import adminVentana
from config.iconos import Iconos

if __name__ == "__main__":
    iconos = Iconos()
    app = adminVentana(iconos=iconos)
    app.run()
