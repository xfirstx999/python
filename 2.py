tagi = input("Podaj tagi rozdzielone przecinkami: ".strip())
lista_tagow = tagi.split(",")
unikalne_tagi = set(lista_tagow)
czyste_tagi = []
for i in lista_tagow:
    czyste_tagi.append(i.strip())
unikalne_tagi = set(czyste_tagi)


print(f"Liczba wszystkich tagów: {len(lista_tagow)}")
print(f"Liczba unikalnych tagów: {len(unikalne_tagi)}")

print("Unikalne tagi alfabetycznie:")
for i in sorted(unikalne_tagi):
    print(f"-{i}")