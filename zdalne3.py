import csv


def wczytaj_pracownikow(sciezka_pliku: str) -> list:
    pracownicy = []

    try:
        with open(sciezka_pliku, "r", newline="", encoding="utf-8") as f:
            czytnik = csv.DictReader(f)

            for wiersz in czytnik:
                try:
                    wiersz["pensja"] = int(wiersz["pensja"])
                    pracownicy.append(wiersz)
                except ValueError:
                    print(f"Ostrzeżenie: nieprawidłowa pensja dla {wiersz['imie']}")

    except FileNotFoundError:
        print("Błąd: plik nie został znaleziony.")

    return pracownicy

if __name__ == "__main__":
    wynik = wczytaj_pracownikow("pracownicy.csv")

    for pracownik in wynik:
        print(pracownik)
