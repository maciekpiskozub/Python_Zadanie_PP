import random

class Tablica:
    def __init__(self, N):
        self.tablica = [0] * N

    # Wypełniamy tablice losowymi liczbami
    # Przykladowe wywolanie metody wypelnij --> tablica.wypelnij(1,100)
    def wypelnij(self, a, b):
        self.tablica = [random.randint(a, b) for i in range(len(self.tablica))]

    # Metoda zwracajaca najwieksza liczbe w tablicy
    def maksimum(self):
        return max(self.tablica)

    # Metoda zwracajaca najmniejsza liczbe w tablicy
    def minimum(self):
        return min(self.tablica)

    # Metoda zwracajaca druga najwieksza liczbe w tablicy
    def maksimum2(self):
        return sorted(set(self))[-2]

    # Metoda zwracajaca index a lub -1 w przypadku braku tej wartosci
    def znajdz(self, a):
        return self.tablica.index(a) if a in self.tablica else -1

# Okreslam, jaki rozmiar ma miec tablica
tablica = Tablica(10)
# Wypelniam ja 10-oma liczbami w zakresie 40-55
tablica.wypelnij(40, 55)



# Wywolujemy wszystkie metody
print("Liczby w tablicy:", tablica.tablica)
print("Maksimum:", tablica.maksimum())
print("Minimum:", tablica.minimum())
print("2nd Maksimum", tablica.maksimum())
print("Znajdz element np. 50:", tablica.znajdz(50))



