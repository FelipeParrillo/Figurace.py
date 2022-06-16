
import json
from tkinter import CENTER
import PySimpleGUI as sg
from resources.config import DIFICULTADES_DEFAULT, USUARIOS_ROOT

#-------------------#
#       Logica      #
#-------------------#


def save_dificultad(usuario, lvl, values):
    """Guarda la configuracion de la dificultad personalizada del usuario y tmb guarda la ultima dificultad que dejo seleccionado el usuario"""
    with open(USUARIOS_ROOT, 'r')as usuarios:
        data = json.load(usuarios)
    if usuario in data:
        if lvl == 'personalizado':
            data[usuario]['config']['rondas'] = values['-rounds-']
            data[usuario]['config']['tiempo'] = values['-time-']
            data[usuario]['config']['acierto'] = values['-points_win-']
            data[usuario]['config']['error'] = values['-points_lose-']
            data[usuario]['config']['pistas'] = values['-clue-']
        data[usuario]['config']['dificultad'] = lvl
    with open(USUARIOS_ROOT, 'w')as usuarios:
        json.dump(data, usuarios)


def lectura_completa(usuario):
    """Retorna todos los datos del usuario que le pases (edad, genero, puntajes, config)"""
    with open(USUARIOS_ROOT, 'r')as usuarios:
        data = json.load(usuarios)
    return data[usuario]


def lectura(usuario):
    """Retorna la configuracion del usuario (rondas, tiempo, ganadas, perdidas, pistas) y su ultima dificultad jugada"""
    with open(USUARIOS_ROOT, 'r')as usuarios:
        data = json.load(usuarios)
    return data[usuario]['config']



def set_dificultad(dificultad, usuario, window):
    """Modifica los Slider en base al boton de dificultad seleccionado"""
    config_default = DIFICULTADES_DEFAULT
    if dificultad in config_default.keys():
        slider_set(config_default[dificultad]['rondas'], config_default[dificultad]['tiempo'], config_default[dificultad]['acierto'],
                   config_default[dificultad]['error'], config_default[dificultad]['pistas'], window)
        act_color(dificultad, window)
    if dificultad == 'personalizado':
        data = lectura(usuario)
        act_color(dificultad, window)
        slider_set(data['rondas'], data['tiempo'],
                   data['acierto'], data['error'], data['pistas'], window)
        slider_reset(window)


def slider_reset(window):
    """Restablece los sliders para que se puedan modificar (se usa dentro de set_dificultad)"""
    window['-rounds-'].update(disabled=False)
    window['-time-'].update(disabled=False)
    window['-points_win-'].update(disabled=False)
    window['-points_lose-'].update(disabled=False)
    window['-clue-'].update(disabled=False)


def slider_set(rondas, tiempo, ganados, perdidos, pistas, window):
    """Modifica los valores de los slider (usada dentro de set_dificultad)"""
    window['-rounds-'].update(rondas, disabled=True)
    window['-time-'].update(tiempo, disabled=True)
    window['-points_win-'].update(ganados, disabled=True)
    window['-points_lose-'].update(perdidos, disabled=True)
    window['-clue-'].update(pistas, disabled=True)


def act_color(dificultad, window):
    """Funcion para actualizar los colores de los botones (usada dentro de set_dificultad)"""
    niveles = ['facil', 'normal', 'dificil', 'experto', 'personalizado']
    for n in niveles:
        if dificultad == n:
            window[n].update(button_color='#273E5B')
        else:
            window[n].update(button_color='#516F95')


#-------------------#
#       Layouts     #
#-------------------#


def botones_layout(dificultad):
    """Inicializa los botones segun el registro anterior"""
    niveles = ['facil', 'normal', 'dificil', 'experto', 'personalizado']
    nombres = ['Facil', 'Normal', 'Dificil', 'Experto', 'Personalizado']
    lista_botones = []
    c = 0
    for n in niveles:
        if dificultad == n:
            lista_botones.append(
                sg.Button(button_text=nombres[c], key=n, button_color=('#273E5B')))
        else:
            lista_botones.append(
                sg.Button(button_text=nombres[c], key=n, button_color=('#516F95')))
        c += 1
    return lista_botones


def slider_layout(dificultad, datos):
    """Modifica los Sliders segun la dificultad enviada"""
    config = DIFICULTADES_DEFAULT
    lista_dificultades_sliders = []
    if dificultad == 'personalizado':
        lista_dificultades_sliders.append([sg.Slider(key='-rounds-',      default_value=datos['rondas'], range=(3, 24), size=(20, 10),
                   enable_events=True, orientation='h', disabled=False),      sg.Text('Cantidad de Rondas', auto_size_text=True)])
        lista_dificultades_sliders.append([sg.Slider(key='-time-',        default_value=datos['tiempo'], range=(30, 120), size=(20, 10),
                   enable_events=True, orientation='h', disabled=False),   sg.Text('Segundos por ronda', auto_size_text=True)])
        lista_dificultades_sliders.append([sg.Slider(key='-points_win-',  default_value=datos['acierto'], range=(1, 10), size=(20, 10), enable_events=True,
                   orientation='h', disabled=False),     sg.Text('Puntaje sumado por Respuesta Correcta', auto_size_text=True)])
        lista_dificultades_sliders.append([sg.Slider(key='-points_lose-', default_value=datos['error'], range=(0, 10), size=(20, 10), enable_events=True,
                   orientation='h', disabled=False),       sg.Text('Puntaje restado por Respuesta Incorrecta', auto_size_text=True)])
        lista_dificultades_sliders.append([sg.Slider(key='-clue-',        default_value=datos['pistas'], range=(2, 5), size=(20, 10), enable_events=True,
                   orientation='h', disabled=False),        sg.Text('Cantidad de Caracteristicas por Ronda', auto_size_text=True)])
    else:
        lista_dificultades_sliders.append([sg.Slider(key='-rounds-',      default_value=config[dificultad]['rondas'], range=(3, 24), size=(20, 10),
                   enable_events=True, orientation='h', disabled=True),      sg.Text('Cantidad de Rondas', auto_size_text=True)])
        lista_dificultades_sliders.append([sg.Slider(key='-time-',        default_value=config[dificultad]['tiempo'], range=(30, 120), size=(20, 10),
                   enable_events=True, orientation='h', disabled=True),   sg.Text('Segundos por ronda', auto_size_text=True)])
        lista_dificultades_sliders.append([sg.Slider(key='-points_win-',  default_value=config[dificultad]['acierto'], range=(1, 10), size=(20, 10),
                   enable_events=True, orientation='h', disabled=True),     sg.Text('Puntaje sumado por Respuesta Correcta', auto_size_text=True)])
        lista_dificultades_sliders.append([sg.Slider(key='-points_lose-', default_value=config[dificultad]['error'], range=(0, 10), size=(20, 10), enable_events=True,
                   orientation='h', disabled=True),       sg.Text('Puntaje restado por Respuesta Incorrecta', auto_size_text=True)])
        lista_dificultades_sliders.append([sg.Slider(key='-clue-',        default_value=config[dificultad]['pistas'], range=(2, 5), size=(20, 10),
                   enable_events=True, orientation='h', disabled=True),        sg.Text('Cantidad de Caracteristicas por Ronda', auto_size_text=True)])

    return lista_dificultades_sliders


def configuracion_layout(usuario):
    """Layout de configuracion"""
    data = lectura(usuario)
    layout = [[sg.Text('Menu de Configuracion', size=(50, 2), justification=CENTER), sg.Button('Menu', key='-menu-')],
              [botones_layout(data['dificultad']),
               sg.Text(f'Usuario: {usuario}')],
              [slider_layout(data['dificultad'], data)],
              [sg.Button('Guardar', key='-save-')]
              ]
    return layout


#-----------------------------------#
#       Handler Config              #
#-----------------------------------#


def handler_config(values, usuario):
    window = sg.Window("Image Viewer", configuracion_layout(values['-usuario-']))
    lvl = lectura(usuario)['dificultad']
    dificultades = ['facil', 'normal','dificil', 'experto', 'personalizado']
    while True:
                event, values = window.read()
                if event == "-menu-" or event == sg.WIN_CLOSED:         # salida
                    window.close()
                    break

                elif event == '-save-':  # guardado
                    save_dificultad(usuario, lvl, values)
                    [sg.Popup('Configuracion Guardada'),sg.Button('OK', key='-menu-')]
                    window.close()
                    break

                elif event in dificultades:  # evento botones de dificultad, sliders y colores de botones
                    lvl = event
                    set_dificultad(event, usuario, window)
                    window.refresh()