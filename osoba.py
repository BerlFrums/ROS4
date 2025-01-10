
class Osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.penize = 100
        self.inventar = {}
        self.max_velikost_inventare = 2

    def koupit_predmet(self, nazev_predmetu, lokace):
        if nazev_predmetu in lokace.predmety:
            predmet = lokace.predmety[nazev_predmetu]
            if self.penize >= predmet.aktualni_cena and len(self.inventar) < self.max_velikost_inventare:
                self.penize -= predmet.aktualni_cena
                self.inventar[nazev_predmetu] = self.inventar.get(nazev_predmetu, 0) + 1
                print(f"Koupil jsi {nazev_predmetu} za {predmet.aktualni_cena} Kč.")
            else:
                print("Nemáš dost peněz nebo místo v inventáři!")

    def prodat_predmet(self, nazev_predmetu, lokace):
        if nazev_predmetu in self.inventar and self.inventar[nazev_predmetu] > 0:
            predmet = lokace.predmety[nazev_predmetu]
            self.penize += predmet.aktualni_cena
            self.inventar[nazev_predmetu] -= 1
            if self.inventar[nazev_predmetu] == 0:
                del self.inventar[nazev_predmetu]
            print(f"Prodal jsi {nazev_predmetu} za {predmet.aktualni_cena} Kč.")
        else:
            print("Nemáš dost peněz na toto vylepšení.")

    def koupit_vylepseni(self, typ_vylepseni, cena):
        if self.penize >= cena:
            self.penize -= cena:
            if typ_vylepseni == "kabát":
                self.max_velikost_inventare += 2
            elif typ_vylepseni == "batoh":
                self.max_velikost_inventare += 3
            print(f"Koupil jsi }{typ_vylepseni}. Kapacita inventáře zvětšena!")
        else:
            print("Nemáš dost peněz na toto vylepšení.")