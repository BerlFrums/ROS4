print()
input("Pro spuštění tutorialu stiskni ENTER")
print()
print("Lokace vybíráš pomocí čísel 1 až 4.")
print()
print("Pokud budeš chtít zakoupit předmět, tak zadej písmeno: K")
print("Pokud budeš chtít prodat předmět, tak zadej písmeno: P")
print("Pokud chceš jít dál, tak zadej písmeno: J")
print()
print("V inventáři máš místo pouze pro 2 předměty.")
print("Jméno předmětu, který chceš zakoupit nebo prodat musíš napsat přesně tak, jak je uvedeno na skladě.")
print("Stejně tak můžeš nakupovat ve večerce vylepšení, jako je kabát a batoh.")
print("Kabát ti rozšíří inventář o 2 předměty a batoh o 3.")
print("Cena kabátu je 150 Kč a batohu 400 Kč.")
print()
input("Pro spuštění hry stiskni ENTER")


from lokace import Lokace
from predmet import Predmet
from osoba import Osoba


# Inicializace lokací a předmětů
predmety = {
    "Utopenec": Predmet("Utopenec", 50, 100),
    "Med": Predmet("Med", 100, 200),
    "Láhev Pálavy": Predmet("Láhev Pálavy", 200, 500),
}

lokace = [
    Lokace("Hradčany", predmety.copy()),
    Lokace("Václavák", predmety.copy()),
    Lokace("Holešovice", predmety.copy()),
    Lokace("Večerka", {}),
]


def main():
    hrac = Osoba("")
    dny = 0

    while dny < 14:
        print()  # Prázdný řádek oddělující dny
        inventar_obsah = " a v inventáři nic" if not hrac.inventar else " a v inventáři " + " a ".join(hrac.inventar.keys())
        print(f"Den {dny + 1}. Máš {hrac.penize} Kč{inventar_obsah}.")
        print("Lokace: 1. Hradčany  2. Václavák  3. Holešovice  4. Večerka")
        while True:
            try:
                volba = int(input("Vyber lokaci (1-4): ")) - 1
                if volba in range(4):
                    break
                else:
                    print("Zadej číslo mezi 1 a 4.")
            except ValueError:
                print("Zadej platné číslo.")

        if volba in range(3):
            aktualni_lokace = lokace[volba]
            aktualni_lokace.aktualizovat_ceny()
            aktualni_lokace.zobrazit_predmety()

            while True:
                akce = input("Chceš (K)oupit, (P)rodat nebo (J)ít dál? ").lower()
                if akce in ["k", "p", "j"]:
                    break
                else:
                    print("Neplatná volba! Zadej 'K', 'P' nebo 'J'.")

            if akce == "k":
                while True:
                    nazev_predmetu = input("Zadej název předmětu k nákupu: ")
                    if nazev_predmetu in aktualni_lokace.predmety:
                        hrac.koupit_predmet(nazev_predmetu, aktualni_lokace)
                        break
                    else:
                        print("Neplatný název předmětu! Zkus to znovu.")
            elif akce == "p":
                while True:
                    nazev_predmetu = input("Zadej název předmětu k prodeji: ")
                    if nazev_predmetu in hrac.inventar:
                        hrac.prodat_predmet(nazev_predmetu, aktualni_lokace)
                        break  # Úspěšný prodej, ukončíme smyčku
                    else:
                        print("Nevlastníš tento předmět!")
                        break  # Přerušíme smyčku a posuneme den


        elif volba == 3:  # Večerka
            print("Vylepšení k dispozici: Kabát (150 Kč), Batoh (400 Kč)")
            while True:
                vylepseni = input("Chceš koupit Kabát nebo Batoh? ").lower()
                if vylepseni in ["kabát", "batoh"]:
                    break
                else:
                    print("Neplatná volba! Zadej 'Kabát' nebo 'Batoh'.")
            if vylepseni == "kabát":
                hrac.koupit_vylepseni("kabát", 150)
            elif vylepseni == "batoh":
                hrac.koupit_vylepseni("batoh", 400)

        dny += 1

    jmeno_hrace = input("Zadej své jméno: ")
    hrac.jmeno = jmeno_hrace
    print("Konec hry!")
    print(f"Konečný počet peněz: {hrac.penize} Kč.")

    with open("highscores.txt", "a", encoding="utf-8") as soubor:
        soubor.write(f"{hrac.jmeno}: {hrac.penize} Kč\n")

    print("Nejlepší výsledky:")
    with open("highscores.txt", "r", encoding="utf-8") as soubor:
        vysledky = []
        for radek in soubor:
            jmeno, penize = radek.rsplit(": ", 1)
            penize = int(penize.replace(" Kč", ""))
            vysledky.append((jmeno, penize))

    vysledky.sort(key=lambda x: x[1], reverse=True)

    for index, (jmeno, penize) in enumerate(vysledky, start=1):
        print(f"{index}. {jmeno}: {penize} Kč")

if __name__ == "__main__":
    main()