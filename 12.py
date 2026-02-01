system_plikow = {
    "typ": "katalog",
    "zawartosc": [
        {"typ": "plik", "rozmiar": 100},
        {
            "typ": "katalog",
            "zawartosc": [
                {"typ": "plik", "rozmiar": 50},
                {"typ": "plik", "rozmiar": 150}
            ]
        },
        {"typ": "plik", "rozmiar": 200}
    ]
}

def oblicz_rozmiar_katalogu(katalog):
    if katalog["typ"] == "plik":
        return katalog["rozmiar"]

    suma = 0
    if katalog["typ"] == "katalog":
        for element in katalog["zawartosc"]:
            suma += oblicz_rozmiar_katalogu(element)

    return suma

print(oblicz_rozmiar_katalogu(system_plikow))

