# Imports #
from tkinter import CENTER
import PySimpleGUI as sg
from resources.screens.jugar import handler_jugar
from resources.screens.usuarios import handler_usuario
from resources.screens.configuracion import handler_config
from resources.screens.puntajes import handler_puntaje
from resources.screens.usuarios import lista_usuarios


def menu_layout(usuario):
    """Layout de menu, verifica que se haya elegido algun usuario valido para jugar o cambiar su configuracion"""

    #sg.theme("Reds")
    if usuario == 'Elije un perfil para jugar...':  # verifica si ya se eligio previamente un usuario o no
        boolean = True
    else:
        boolean = False

    x = 50
    y = 2
    layout = [
        [sg.Text('FiguRace', size=(x, y), justification=CENTER)],
        [sg.Text('Usuario:'), sg.Combo(enable_events=True, values=(lista_usuarios(
        )), key='-usuario-', default_value=usuario, size=(25, 10), auto_size_text=True)],
        [sg.Button('Jugar', size=(x, y), key="-play-", disabled=boolean)],
        [sg.Button('Configuración', size=(x, y),
                   key="-settings-", disabled=boolean)],
        [sg.Button('Puntaje', size=(x, y), key="-score-")],
        [sg.Button('Perfil', size=(x, y), key="-user-")],
        [sg.Button('Salir', size=(x, y), key="-exit-")]
    ]
    return layout


def menu_start_up():
    """Inicializacion de la app"""
    usuario = 'Elije un perfil para jugar...'  # variable de instancia para mantener el sg.combo

    window = sg.Window("Image Viewer", menu_layout(usuario))
    while True:
        event, values = window.read()

        #-------------------#
        #       Menu        #
        #-------------------#
        if event == "-exit-" or event == sg.WIN_CLOSED:  # Evento de salida
            break

        if event == '-menu-':  # Evento para ir al menu principal
            window.close()
            window = sg.Window("Image Viewer", menu_layout(usuario))

        if event == '-usuario-':  # seleccion de usuario para jugar o configurar la dificultad
            window['-play-'].Update(disabled=False)
            window['-settings-'].Update(disabled=False)
            usuario = values['-usuario-']
            window.refresh()

        #-----------------------#
        #       Usuarios        #
        #-----------------------#

        #___Iniciacion Layout Usuario___#
        if event == '-user-':
            window.close()
            handler_usuario()
            window = sg.Window("Image Viewer", menu_layout(usuario))

        #-----------------------#
        #       Puntajes        #
        #-----------------------#
        if event == '-score-':
            window.close()
            handler_puntaje(usuario)
            window = sg.Window("Image Viewer", menu_layout(usuario))

        #---------------------------#
        #       Configuracion       #
        #---------------------------#
        if event == '-settings-': 
            window.close()
            handler_config(values,usuario)
            window = sg.Window("Image Viewer", menu_layout(usuario))

        #---------------------------#
        #           Jugar           #
        #---------------------------#
        if event == '-play-':
            if usuario in lista_usuarios():
                window.close()
                handler_jugar(usuario)
                window = sg.Window("Image Viewer", menu_layout(usuario))
                
            else:
                window.close()
                window = sg.Popup('El usuario que había seleccionado, ya no existe..')
                usuario = 'Elije un perfil para jugar...'
                window = sg.Window("Image Viewer", menu_layout(usuario))
