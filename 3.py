kontakty = {}

while True:
    opcja = input(f"Wybierz opcje: (dodaj,wyświetl kontakt,usuń,wyświetl wszystko lub 'koniec'):")
    if opcja.lower() == "koniec":
        break
    elif opcja.lower() == "dodaj":
        nazwa = input("Podaj nazwę: ")
        if nazwa not in kontakty:
            numer = input("Podaj numer: ")
            kontakty[nazwa] = numer
        else:
            print("Jest już taka osoba")
    elif opcja.lower() == "wyświetl kontakt":
        nazwa = input("Podaj nazwę: ")
        if nazwa in kontakty:
            print(f"Numer do {nazwa} to {kontakty[nazwa]}")
        else: print(f"Nie ma takiej osoby")
    elif opcja.lower() == "usuń":
        nazwa = input("Podaj nazwę: ")
        if nazwa in kontakty:
            del(kontakty[nazwa])
            print(f"Usunięto {nazwa} z kontaków")
        else: print(f"Nie ma takiej osoby")
    elif opcja.lower() == "wyświetl wszystko":
        print("---MOJE KONTAKTY---")
        for nazwa, numer in kontakty.items():
            print(f"Nazwa: {nazwa}, numer: {numer}")
        print("---KONIEC LISTY---")
    elif opcja.lower() == "koniec":
        break
    else:
        print("Niepoprawna opcja")