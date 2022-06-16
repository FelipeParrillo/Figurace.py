


from resources.config import DIFICULTADES_DEFAULT


class Jugador:
    CONFIG_DEFAULT = DIFICULTADES_DEFAULT

    def __init__(self, nom, val):
        self._nombre = nom
        self._valores = val
        self._puntaje_actual = 0
        self._respuesta_actual = ''

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nom):
        self._nombre = nom

    def get_valores(self):
        return self._valores

    def set_valores(self, val):
        self._valores = val

    def get_config_default(self):
        return self.CONFIG_DEFAULT

    def incrementar_puntaje_actual(self, num):
        self._puntaje_actual = self.get_puntaje_actual() + num
        
    def decrementar_puntaje_actual(self,num):
        self._puntaje_actual = self.get_puntaje_actual() - num
        
    def get_puntaje_actual(self):
        return self._puntaje_actual

    def get_respuesta_actual(self):
        return self._respuesta_actual

    def set_respuesta_actual(self, respuesta):
        self._respuesta_actual = respuesta


