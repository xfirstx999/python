def analizuj_grupe(czlonkowie, prog_stypendium):

    if len(czlonkowie) == 0:
        return {
            "imie": None,
            "srednia_ocen": None,
            "kierunek": None,
        }

    suma_srednich = 0
    for i in czlonkowie:
        suma_srednich += i["srednia_ocen"]
        srednia = suma_srednich / len(czlonkowie)

    najlepszy_student = czlonkowie[0]
    for i in czlonkowie:
        if i["srednia_ocen"] > najlepszy_student["srednia_ocen"]:
            najlepszy_student = i
    imie = najlepszy_student["imie"]

    unikalne_kierunki = set()
    for i in czlonkowie:
        unikalne_kierunki.add(i["kierunek"])

    stypendium_grupowe = srednia > prog_stypendium

    return {
        "srednia_ocen": srednia,
        "najlepszy_student": imie,
        "unikalne_kierunki": unikalne_kierunki,
        "stypendium_grupowe": stypendium_grupowe
    }



studenci = [
    {"imie": "Anna", "srednia_ocen": 4.5, "kierunek": "Informatyka"},
    {"imie": "Piotr", "srednia_ocen": 3.8, "kierunek": "Automatyka"},
    {"imie": "Zofia", "srednia_ocen": 4.9, "kierunek": "Informatyka"}
]

lista = [len(x["imie"]) for x in studenci if x["kierunek"] == "Informatyka"]

wynik = analizuj_grupe(studenci, 4.2)
print(wynik)
print(lista)