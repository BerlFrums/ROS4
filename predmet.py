import random

class Predmet:
    def __init__(self, nazev, min_cena, max_cena):
        self.nazev = nazev
        self.min_cena = min_cena
        self.max_cena = max_cena
        self.aktualni_cena = random.randint(min_cena, max_cena)

    def aktualizovat_cenu(self):
        zmena = random.randint(-5, 5)
        self.aktualni_cena = max(self.min_cena, min(self.max_cena, self.aktualni_cena + zmena))