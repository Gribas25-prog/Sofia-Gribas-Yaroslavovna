import sys
from .zagruzka_dannyh import ZagruzkaDannyh
from .statistika_pogody import StatistikaPogody

def main():
    if len(sys.argv) < 2:
        print("Использование analiz-pogody data.csv")
        return

    put = sys.argv[1]
    loader = ZagruzkaDannyh(put)
    dannye = loader.zagruzit()
    statistika = StatistikaPogody(dannye)
    print(statistika.otchet())

if __name__ == "__main__":
    main()
