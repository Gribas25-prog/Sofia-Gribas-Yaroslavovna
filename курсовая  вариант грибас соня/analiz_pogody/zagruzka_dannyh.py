#загрузка из CSV файла
import csv
from .den_pogody import DenPogody
class ZagruzkaDannyh:
    def __init__(self, put_k_failu: str):
        self.put_k_failu = put_k_failu
    def zagruzit(self):
        dni = []
        with open(self.put_k_failu, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for stroka in reader:
                den = DenPogody(
                    data=stroka["date"],
                    temperatura=float(stroka["temperature"]),
                    vlazhnost=float(stroka["humidity"]),
                    osadki=float(stroka["precipitation"])
                )
                dni.append(den)

        return dni
