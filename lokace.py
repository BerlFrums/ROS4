class Lokace:
    def __init__(self, nazev, predmety):
        self.nazev = nazev
        self.predmety = predmety  # Slovník predmetů {nazev_predmetu: objekt Predmet}

    def zobrazit_predmety(self):
        print(f"Předměty dostupné v lokaci {self.nazev}:")
        for predmet in self.predmety.values():
            print(f"{predmet.nazev}: {predmet.aktualni_cena} Kč")

    def aktualizovat_ceny(self):
        for predmet in self.predmety.values():
            predmet.aktualizovat_cenu()