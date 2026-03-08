from statistics import mean

class StatistikaPogody:
    def __init__(self, dni_pogody):
        self.dni_pogody = dni_pogody
    def max_temperatura(self):
        return max(den.temperatura for den in self.dni_pogody)
    def min_temperatura(self):
        return min(den.temperatura for den in self.dni_pogody)
    def srednyaya_temperatura(self):
        return mean(den.temperatura for den in self.dni_pogody)
    def summa_osadkov(self):
        return sum(den.osadki for den in self.dni_pogody)
    def trend_temperatury(self):
        temp = [d.temperatura for d in self.dni_pogody]

        if temp[-1] > temp[0]:
            return "Температура повыш"
        elif temp[-1] < temp[0]:
            return "Температура пониж"
        return "Температура стабильна"

    def otchet(self):
        return f"""
Отчет 
Макc темп {self.max_temperatura()}
Мин темп {self.min_temperatura()}
Средняя темпер: {self.srednyaya_temperatura():.2f}
Сумма осадков: {self.summa_osadkov()}
Тенденция темпы: {self.trend_temperatury()}

