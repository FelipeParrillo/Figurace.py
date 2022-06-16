from tkinter import CENTER, LEFT
import PySimpleGUI as sg
from resources.screens.jugar import color_boton
from resources.screens.usuarios import read_data



#-----------------------------------#
#       Usuarios Modificaciones     #
#-----------------------------------#



def puntajes_ordenados(criterio):
    """Retorna un String con todos los usuarios ordenados por puntaje y una dificultad especifica"""
    usuarios = read_data()
    lista = [[usuarios[usu]['puntajes'][criterio], usu] for usu in usuarios]
    ordenada = sorted(lista, reverse=True)
    
    # Cabecera de la tabla puntajes
    tabla = "Posicion   |       Nombre:Puntaje  \n"
    tabla+='--------------------------------------------------\n'                             
    for usuario in enumerate(ordenada[0:20]):
        tabla += f'{str(usuario[0]+1)+"°":<14} {"|":<3} {""+str(usuario[1][1])+":"+str(usuario[1][0]):<20}\n'
        tabla+='--------------------------------------------------\n'
    return tabla.strip()



def actualizar_ventana(dificultad, window):
    """Actualiza la ventana de puntajes con su dificultad correspondiente"""
    window['dat'].update(puntajes_ordenados(dificultad))


def cambiar_dificultad(dificultad, window):
    """Le envia a la funcion Actualizar, la dificultad elegida por el usuario"""
    match dificultad:
        case '-easy-':
            actualizar_ventana('facil', window)
        case '-normal-':
            actualizar_ventana('normal', window)
        case '-hard-':
            actualizar_ventana('dificil', window)
        case '-expert-':
            actualizar_ventana('experto', window)
        case '-custom-':
            actualizar_ventana('personalizado', window)

#-----------------------------------#
#       Puntaje  Layouts            #
#-----------------------------------#

def puntajes_layout():
    layout = [
        [sg.Text('Menu de Puntajes', size=(50, 2), justification=CENTER,
                 auto_size_text=True), sg.Button('Menu', key='-menu-', auto_size_button=True)],
        [sg.Button('Facil', key='-easy-', button_color=('#516F95')), sg.Button('Normal', key='-normal-', button_color=('#516F95')), sg.Button('Dificil', key='-hard-',
                                                                                                                                              button_color=('#516F95')), sg.Button('Experto', key='-expert-', button_color=('#516F95'),), sg.Button('Personalizado', key='-custom-', button_color=('#273E5B'))],
        [[sg.Text('      Top 20 de puntajes     ')], sg.Multiline(default_text=puntajes_ordenados(
            'personalizado'), key='dat', size=(29, 27), auto_size_text=True, justification=LEFT)],
    ]
    return layout


#-----------------------------------#
#       Handler Puntaje             #
#-----------------------------------#


def handler_puntaje(usuario):
    dificultades = ['-easy-', '-normal-','-hard-', '-expert-', '-custom-']
    window = sg.Window("Image Viewer", puntajes_layout(), size=(500,500)).Finalize()
    ml_pj = window["dat"]
    ml_pj.Update(disabled=True)
    lvl = '-custom-'
    while True:
        event, values = window.read()
        
        if event == '-menu-' or event == sg.WIN_CLOSED: # salida a menu
            window.close()
            break
        
        elif event in dificultades:
            buttons = [ window['-easy-'], window['-normal-'],
                        window['-hard-'], window['-expert-'], window['-custom-']]
            choosen = window[event]
            color_boton(choosen,buttons)
            lvl = event
            cambiar_dificultad(event,window)
            window.refresh()
