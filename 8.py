#pracownicy = [
#    {"imie": "Anna", "stanowisko": "Specjalista", "pensja": 4500},
#    {"imie": "Piotr", "stanowisko": "Menager", "pensja": 8000},
#    {"imie": "Zofia", "stanowisko": "Specjalista", "pensja": 5200}
#]
#
#lista_plac = [i["pensja"] for i in pracownicy if i["stanowisko"] == "Specjalista"]
#
#print(f"Lista płac dla specjalistów: {lista_plac}")

zduplikowane_dane = [
    {"id": 1, "imie": "Anna"},
    {"id": 2, "imie": "Piotr"},
    {"id": 1, "imie": "Anna"},
    {"id": 3, "imie": "Zofia"},
]

widziane = set()
unikalne = [(osoba["id"], osoba["imie"]) for osoba in zduplikowane_dane
            if not (osoba["id"] in widziane or widziane.add(osoba["id"]))]

print(unikalne)