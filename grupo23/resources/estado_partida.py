class Estado_partida:

    def __init__(self, rondas, dificultad):
        self._estado = {"iniciada": False, "finalizada": False, "abandonada": False}
        self._total_rondas = rondas
        self._ronda_actual = 1
        self._timer_iniciado = False
        self._dificultad = dificultad

    def get_estado(self, key):
        return self._estado[key]

    def get_timer_iniciado(self):
        return self._timer_iniciado

    def get_dificultad(self):
        return self._dificultad
    
    def get_total_rondas(self):
        return self._total_rondas
    
    def get_ronda_actual(self):
        return self._ronda_actual

    def set_estado(self, key, nuevo_estado):
        self._estado[key] = nuevo_estado
    
    def set_dificultad(self, nueva_dificultad):
        self._dificultad = nueva_dificultad
    
    def set_timer_iniciado(self):
        self._timer_iniciado = True

    def set_total_rondas(self, tot):
        self._total_rondas = tot

    def incrementar_ronda_actual(self):
        self._ronda_actual = self.get_ronda_actual() + 1
    