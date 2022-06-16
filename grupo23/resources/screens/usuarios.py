import json
from tkinter import CENTER
import PySimpleGUI as sg
from resources.config import USUARIOS_ROOT


#---------------------------------------#
#       Funciones a la Estructura       #
#---------------------------------------#


def reset_estructura():
    """Crea la estructura en el usuarios.json desde cero"""
    with open(USUARIOS_ROOT, 'w')as usuarios:
        estructura = {}
        json.dump(estructura, usuarios)


def write_data(data):
    """Escribe en usuarios.json"""
    with open(USUARIOS_ROOT, 'w')as usuarios:
        json.dump(data, usuarios)


def read_data():
    """Devuelve toda la estructura almacenada en el usuarios.json"""
    with open(USUARIOS_ROOT, 'r')as usuarios:
        data = json.load(usuarios)
    return data


#-----------------------------------#
#       Usuarios Modificaciones     #
#-----------------------------------#


def delet_usuario(usuario):
    """Borra la clave (Perfil/Usuario) pasada como parametro de la estructura de usuarios.json"""
    data = read_data()
    if usuario in data.keys():
        del data[usuario]
    else:
        [sg.Popup("Error, no se encontro el usuario"),
         sg.Button('Vovler', key='-user-')]
    write_data(data)


def change_usuario(usuario, edad, *generos):
    """Modifica los datos del usuario pasado como parametro invocation: change_usuario(name, age, genre)"""
    data = read_data()
    lista_generos = ['m', 'f', 'x']
    # encuentra la pos de generos que fue seleccionada y lo pasa como texto
    for b in range(len(generos)):
        if generos[b]:
            genero = lista_generos[b]

    if usuario in data.keys():
        data[usuario]['edad'] = int(edad)
        data[usuario]['genero'] = genero
        write_data(data)
        [sg.Popup(f'Datos de {usuario} modificados correctamente'), sg.Button(
            'Volver', key='-user-')]
    else:
        [sg.Popup("Error, no se encontro el usuario"),
         sg.Button('Volver', key='-user-')]


def append_usuario(usuario, edad, genero):
    """Agrega a la estructura usuarios.json el nuevo usuario aprobado invocation: append_usuario(name, age, genre) """
    datos = read_data()
    datos[usuario] = {"edad": edad, "genero": genero, "puntajes": {"facil": 0, "normal": 0,
                                                                   "dificil": 0, "experto": 0, "personalizado": 0},  # Todos inicializados en cero
                      "config": {"rondas": 0, "tiempo": 0, "acierto": 0, "error": 0, "pistas": 0, "dificultad": "facil"}}
    write_data(datos)


def verify_usuario(usuario, edad, *generos):
    """Verifica que los datos ingresados para un nuevo usuario sean aprobados es decir: que se ingrese un nombre, edad, genero y que el nombre de usuario no este repetido invocation: verify_usuario(name, age, genre)"""
    lista_generos = ['m', 'f', 'x']
    # encuentra la pos de generos que fue seleccionada y lo pasa como texto
    for b in range(len(generos)):
        if generos[b]:
            genero = lista_generos[b]

    data = read_data()
    # Ordenamiento de Strings al standar (sin espacios antes o despues, mayuscula en la primera letra de cada palabra, todo lo demas en minuscula)
    usuario = usuario.strip().lower().title()
    if (usuario != '') and (usuario not in data.keys()):  # Validacion de nombre
        # aprobacion de usuario para cargarlo a  usuario.json (CUIDADO QUE ESTE EN USUARIO.JSON NO SIGNIFICA QUE ESTE EN PUNTAJE)
        append_usuario(usuario, int(edad), genero)
        return '-user-'
    else:
        [sg.Popup('El nombre no es valido o ya existe'),
         sg.Button('OK', key='-new_user-')]


#-----------------------#
#        Layouts        #
#-----------------------#


def string_usuarios():
    """Devuelve una string de todos los usuarios"""
    data = read_data()
    usuarios = list(data.keys())
    usuarios.sort()
    string_users = ('\n'.join(usuarios))
    return string_users


def lista_usuarios():
    """Retorna una lista con todos los usuarios"""
    data = read_data()
    usuarios = list(data.keys())
    return usuarios


def nuevo_usuario_layout():
    """Lasyout de un nuevo Usuario"""
    layout = [
        [sg.Text('Creacion de Nuevo Usuario', justification=CENTER)],
        [sg.Text('Ingrese su nombre : '), sg.Input(
            do_not_clear=True, enable_events=True, key='-name-')],
        [sg.Text('Ingrese su edad : '), sg.Slider(orientation='h',
                                                  key='-age-', range=(1, 100), size=(50, 10), default_value=int)],
        [sg.Text('Ingrese su genero : '), sg.Radio('Masculino', "Genero", default=True, size=(10, 1), k='-m-'), sg.Radio('Femenino',
                                                                                                                         "Genero", default=False, size=(10, 1), k='-f-'), sg.Radio('X', "Genero", default=False, size=(10, 1), k='-x-')],
        [sg.Button('Confirmar', key='-add-'),
         sg.Button('Cancelar', key='-user-')]
    ]
    return layout


def eliminar_usuario_layout():
    """Layout para seleccionar un usuario a eliminar"""
    layout = [
        [sg.Text('Eliminacion de Usuarios', size=(50, 2), justification=CENTER)],
        [sg.Listbox(values=lista_usuarios(), size=(20, 12),
                    key='-delet_listbox-', enable_events=True)],
        [sg.Button("Borrar", key='-delet-')],
        [sg.Button('Volver', key='-user-')]
    ]
    return layout


def modificar_usuario_layout():
    """Layout para seleccionar un usuario a modificar"""
    layout = [
        [sg.Text('Modificacion de Usuarios', size=(50, 2), justification=CENTER)],
        [sg.Listbox(values=lista_usuarios(), size=(20, 12),
                    key='-THEME LISTBOX-', enable_events=True)],
        [sg.Button("Modificar", key='-mod-')],
        [sg.Button('Volver', key='-user-')]
    ]
    return layout


def change_layout():
    """Layout para cambiar datos de un usuario"""
    layout = [
        [sg.Text('Ingrese su nueva edad : '), sg.Slider(orientation='h', key='-age-', range=(1, 100),
                                                        size=(50, 10), default_value=int), sg.Button('Volver', key='-modify_user-', size=(5, 2))],
        [sg.Text('Ingrese su nuevo genero : '), sg.Radio('Masculino', "RadioDemo", default=True, size=(10, 1), k='-m-'), sg.Radio('Femenino',
                                                                                                                                  "RadioDemo", default=False, size=(10, 1), k='-f-'), sg.Radio('X', "RadioDemo", default=False, size=(10, 1), k='-x-')],
        [sg.Button('Confirmar', key='-change-')]
    ]
    return layout


def usuarios_layout():
    """Layout para la creacion de un nuevo usuario"""
    layout = [[sg.Text('Menu de Usuarios', size=(50, 2), justification=CENTER, auto_size_text=True), sg.Button('Menu', key='-menu-', auto_size_button=True)],
              [sg.Button('Nuevo Usuario', key='-new_user-', auto_size_button=True), sg.Button('Modificar Usuario',
                                                                                              auto_size_button=True, key='-modify_user-'), sg.Button('Eliminar Usuario', key='-delet_user-', auto_size_button=True)],
              [sg.Text('Perfiles Existentes')],
              [sg.Multiline(default_text=string_usuarios(),
                            key='ml', size=(16, 13), auto_size_text=True)],
              ]
    return layout


#-----------------------------------#
#       Handler Usuario             #
#-----------------------------------#


def handler_usuario():
    window = sg.Window("Image Viewer", usuarios_layout()).Finalize()
    ml_obj = window["ml"]
    ml_obj.Update(disabled=True)
    while True:
        event, values = window.read()
        if event == '-new_user-':  # Layout para carga de nuevos usuarios
                window.close()
                window = sg.Window("Image Viewer", nuevo_usuario_layout())
        try:
            # Limitador de rango para la introduccion de caracteres en el nombre
            if len(values['-name-']) > 15:
                window.Element('-name-').Update(values['-name-'][:-1])
        except:
            pass

        if event == '-add-':  # Validacion de datos para un nuevo usuario y su creacion en usuarios.json
            llave = verify_usuario(
                values['-name-'], values['-age-'], values['-m-'], values['-f-'], values['-x-'])
            if llave == '-user-':
                window.close()
                [sg.Popup('Usuario Cargado Correctamente'),
                 sg.Button('OK', key='-prueba-')]
                window = sg.Window(
                    "Image Viewer", usuarios_layout()).Finalize()
                multiline_obj = window["ml"]
                multiline_obj.Update(disabled=True)
            
        if event == '-user-':
            window.close()
            window = sg.Window("Image Viewer", usuarios_layout()).Finalize()
            ml_obj = window["ml"]
            ml_obj.Update(disabled=True)
    
         #___Apartado Modificacion de Usuarios___#
        if event == '-modify_user-':  # Layout para cambiar datos de usuarios
            window.close()
            window = sg.Window("Image Viewer", modificar_usuario_layout())

        if event == '-mod-':  # Modificacion de usuarios
            try:
                aux_values = values['-THEME LISTBOX-'][0]
                window.close()
                window = sg.Window("Image Viewer", change_layout())
            except:
                [sg.Popup('No hay un usuario seleccionado para modificar'),
                 sg.Button('OK', key='-modify_user-')]

        if event == '-change-':  # Confirmacion de cambios en un usuario y su guardado en usuarios.json
            change_usuario(
                aux_values, values['-age-'], values['-m-'], values['-f-'], values['-x-'])
            window.close()
            window = sg.Window("Image Viewer", modificar_usuario_layout())

        #___Apartado Eliminacion___#

        if event == '-delet_user-':  # Layout de eliminar Usuarios
            window.close()
            window = sg.Window("Image Viewer", eliminar_usuario_layout())

        if event == '-delet-':  # Evento para eliminar un usuario
            try:
                aux_values = values['-delet_listbox-'][0]
                delet_usuario(aux_values)
            except:
                [sg.Popup('No hay un usuario seleccionado para eliminar'),
                 sg.Button('OK', key='-delet_user-')]
            window.close()
            window = sg.Window("Image Viewer", eliminar_usuario_layout())

        if event == '-menu-' or event == sg.WIN_CLOSED: # salida a menu
            window.close()
            break
