import csv


def zapisz_raport_sprzedazy(sciezka_pliku: str, dane_sprzedazy: list):
    if not dane_sprzedazy:
        print("Brak danych do zapisu.")
        return

    pola = dane_sprzedazy[0].keys()

    with open(sciezka_pliku, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=pola)
        writer.writeheader()
        writer.writerows(dane_sprzedazy)

    print(f"Plik '{sciezka_pliku}' został zapisany poprawnie.")


sprzedaz = [
    {"produkt": "Laptop", "sprzedana_ilosc": 5, "przychody": 25000},
    {"produkt": "Telefon", "sprzedana_ilosc": 10, "przychody": 30000},
    {"produkt": "Tablet", "sprzedana_ilosc": 3, "przychody": 9000},
]

zapisz_raport_sprzedazy("raport.csv", sprzedaz)
