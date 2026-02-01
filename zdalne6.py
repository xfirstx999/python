import json

def zapisz_jako_json(dane: dict | list, sciezka_pliku: str) -> None:
    try:
        with open(sciezka_pliku, 'w', encoding="utf-8") as f:
            json.dump(
                dane,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Plik '{sciezka_pliku}' został poprawnie zapisany.")

    except IOError:
        print(f"Błąd zapisu pliku '{sciezka_pliku}'.")

moje_dane = {
    "imie": "Łukasz",
    "wiek": 25,
    "ulubiony_kolor": "żółty",
    "hobby": ["programowanie", "czytanie", "piłka nożna"]
}
zapisz_jako_json(moje_dane, "dane.json")
