def paragon(produkty, VAT=0.23):
    razem = 0
    print("---PARAGON---")

    for i in produkty:
        z_podatkiem = i["cena_netto"] * (1 + VAT)
        razem += z_podatkiem
        print(f"Cena: {i['nazwa']} z podatkiem VAT: {z_podatkiem:.2f}")
    print(f"Suma produktów: {razem:.2f}")


produkty = [
    {"nazwa": "Mleko", "cena_netto": 3.50},
    {"nazwa": "Czekolada", "cena_netto": 5.20},
]

paragon(produkty)
