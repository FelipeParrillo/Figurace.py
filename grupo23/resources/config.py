import os

ROOT = os.path.dirname(__file__)
DATASET_ROOT = os.path.abspath(os.path.join(ROOT, "files", "datasets_final"))
FILES_ROOT = os.path.abspath(os.path.join(ROOT, "files"))
IMAGES_ROOT = os.path.abspath(os.path.join(ROOT, "files", "images"))
USUARIOS_ROOT = os.path.abspath(os.path.join(ROOT, "usuarios.json"))
CONFIG_JSON_ROOT = os.path.abspath(os.path.join(ROOT, "configuracion.json"))


DIFICULTADES_DEFAULT = {
    "facil": {
        "rondas": 8,
        "tiempo": 100,
        "acierto": 2,
        "error": 0,
        "pistas": 5
    },
    "normal": {
        "rondas": 12,
        "tiempo": 70,
        "acierto": 5,
        "error": 2,
        "pistas": 4
    },
    "dificil": {
        "rondas": 15,
        "tiempo": 45,
        "acierto": 7,
        "error": 4,
        "pistas": 3
    },
    "experto": {
        "rondas": 20,
        "tiempo": 30,
        "acierto": 10,
        "error": 9,
        "pistas": 2
    }}