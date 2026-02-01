import json

def wczytaj_konfiguracje(sciezka: str) -> dict:
    try:
        with open(sciezka, 'r', encoding="utf-8") as f:
            dane_jako_slowinik = json.load(f)
        return dane_jako_slowinik
    except FileNotFoundError:
        print(f"Plik {sciezka} nie istnieje.")
        return {}
    except json.JSONDecodeError:
        print(f"Plik {sciezka} ma niepoprawny format JSON.")
        return {}

config_data = wczytaj_konfiguracje('konfiguracja.json')

if config_data:
    print(config_data['baza_danych']['uzytkownik'])
