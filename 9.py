def analizuj_oceny(dane_studentow):
    suma_ocen = 0
    for osoba in dane_studentow:
        suma_ocen += osoba["ocena"]
        srednia = suma_ocen / len(dane_studentow)

    najlepszy_student = dane_studentow[0]
    for osoba in dane_studentow:
        if osoba["ocena"] > dane_studentow[0]["ocena"]:
            najlepszy_student = osoba

    unikalne = set()
    for osoba in dane_studentow:
        unikalne.add(osoba["ocena"])

    return {
        "średnia ocen": srednia,
        "najlepszy student": najlepszy_student,
        "unikalne oceny": unikalne
    }
dane_studentow = [
    {"imie": "Anna", "ocena": 5},
    {"imie": "Czechia", "ocena": 3},
    {"imie": "Zofia", "ocena": 3},
    {"imie": "Krzyśtof", "ocena": 6},
]

print(analizuj_oceny(dane_studentow))
