#описания одного дня погоды.
class DenPogody:

    def __init__(self, data, temperatura, vlazhnost, osadki):
        self._data = data
        self._temperatura = temperatura
        self._vlazhnost = vlazhnost
        self._osadki = osadki

    @property
    def temperatura(self):
        return self._temperatura

    @property
    def vlazhnost(self):
        return self._vlazhnost

    @property
    def osadki(self):
        return self._osadki

    def __repr__(self):
        return f"{self._data}: {self._temperatura}°C"
