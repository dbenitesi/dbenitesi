#   Program to configure Mikrotiks Devices
#   Author: Daniel Benites
#   Version: 0.0.1
#   Daule - Ecuador

# centered Print
option_main_menu = 0
def main():
    def main_menu():

        print('{:^150s}'.format("BIENVENIDO AL SISTEMA TECNICO DE NEXTCORE"))
        print('{:^150s}'.format("PARA SELECCIONAR UNA OPCION FAVOR DIGITE SY NUMERO\n"))
        print('{:^150s}'.format("MENU DE OPCIONES"))
        print('{:^150s}'.format("1.-CONFIGURAR PTP"))
        print('{:^150s}'.format("2.- CONFIGURAR CPE"))
        print('{:^150s}'.format("3.- CONFIGURAR ROUTER MUNICIPIO PC"))
        print('{:^150s}'.format("4.- CONFIGURAR ROUTER DE ZONA"))
        print('{:^150s}'.format("5.- SALIR\n"))
    main_menu()
    option_main_menu = input('{:^150s}'.format("ESCOJA UNA OPCION"))
    print("Usted ha elegido " + option_main_menu)
    print(type(option_main_menu))

    def config_ptp():
        print('{:^150s}'.format("USTED A ELEGIDO CONFIGURAR UN PTP"))
        print('{:^150s}'.format("EN ESTE PROCESO VAMOS A NECESITAR VARIOS DATOS:"))
        print('{:^150s}'.format("VLAN"))
        print('{:^150s}'.format("IP"))
        print('{:^150s}'.format("NOMBRE DEL PTP"))
        print('{:^150s}'.format("AP O ESTACION"))

    def conf_cpe():
        print("CPE")

    def conf_rmuni():
        print("ROUTER MUNICIPIO")

    def conf_rzona():
        print("Router de zona")

    def selection_main_menu(option):
        if option_main_menu =="1":
            config_ptp()
        elif option_main_menu =="2":
            conf_cpe()
        elif option_main_menu == "3":
            conf_rmuni()
        elif option_main_menu == "4":
            conf_rzona
        elif option_main_menu == "5":
            return()
        else: 
            print("DIGITE UNA OPCION VALIDA")
            main()
    selection_main_menu(option_main_menu)

main()