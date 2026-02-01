zakupy = []
while True:
    produkt = input("Podaj produkt na liste zakupów lub 'koniec': ")
    if produkt.lower() == "koniec":
        break
    else:
        zakupy.append(produkt)
zakupy.sort()
print(f"Liczba produktów: {len(zakupy)}")
for nr,produkt in enumerate(zakupy, start=1):
    print(f"{nr}. {produkt}")
