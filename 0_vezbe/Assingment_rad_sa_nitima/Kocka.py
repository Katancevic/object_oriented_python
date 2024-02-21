import threading


class Kocka(threading.Thread):
    def __init__(self, duz_stranice, zapremina):
        self.duz_stranice = duz_stranice
        self.zapremina = zapremina


    def calc_zapremina(num):
        print(f"Запремина коцке je: {num * num * num}cm3")

    def calc_stranice(num):
        print(f"Укупна дужина страница коцке je: {num + num + num + num}cm")


if __name__ == "__main__":

    k1 = threading.Thread(target=Kocka.calc_stranice, args=(10,))
    k2 = threading.Thread(target=Kocka.calc_zapremina, args=(10,))

k1.start()
k2.start()

k1.join()
k2.join()

print("Завршено!!!")
