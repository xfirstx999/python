baza_danych = [
    {"imie":"Anna", "stanowisko":"Specjalista", "pensja":4500},
    {"imie":"Piotr", "stanowisko":"Menager", "pensja":8000},
    {"imie":"Zofia", "stanowisko":"Specjalista", "pensja":5200},
    {"imie":"Krzysztof", "stanowisko":"Stażysta", "pensja":2500}
]

suma = 0
for i in baza_danych:
    suma += i["pensja"]
srednia = suma/len(baza_danych)
print(f"Średnia zarobków to: {srednia}")

for i in baza_danych:
    if i["stanowisko"] == "Specjalista":
        print(i["imie"], i["stanowisko"], i["pensja"])

max_pensja = 0
for i in baza_danych:
    if i["pensja"] > max_pensja:
        max_pensja = i["pensja"]
print(max_pensja)