import functools
import time
import math

# age = int(input("podaj wiek: "))
# age_int = int(age)
# if(age_int < 13):
#     print("dziecko")
# elif(13 <= age_int < 18):
#     print("nastolatek")
# elif(18 <= age_int < 64):
#     print("dorosly")
# else:
#     print("senior")

# points = int(input("podaj liczbe punktow z kolokwium (0-100): "))
# points_int = int(points)
# if points_int <= 50:
#     print("ocena: 2")
# elif points_int <= 60:
#     print("ocena: 3")
# elif points_int <= 70:
#     print("ocena: 3.5")
# elif points_int <= 80:
#     print("ocena: 4")
# elif points_int <= 90:
#     print("ocena: 4.5")
# elif points_int <= 100:
#     print("ocena: 5")

# wzrost = int(input("podaj wzrost: "))
# wiek = int(input("podaj wiek: "))
# zgoda = (input("czy masz zgode (tak/nie): "))
# if wzrost >= 140 and zgoda.lower() == "tak" or wiek > 18:
#     print("mozesz wejsc")
# else:
#     print("nie mozesz wejsc")

# i = int(5)
# while i > 0:
#     print(i)
#     i -= 1


# while True:
#     i = int(input(": "))
#     if(i == 1):
#         print("sdgsbfd")
#     break

# while True:
#     koniec = input("wpisz koniec: ")
#     if koniec.lower() == "koniec":
#         print("sdfsdb")
#         break
#     if koniec.startswith("#"):
#         print("zly napis")
#         continue

# for litera in "python":
#     print(f"dfbdfb: {litera.upper()}")

# wyraz = input("podaj wyraz: ")
# licznik_samoglosek = int(0)
# samogloski = "aeiouy"
# for litera in wyraz:
#     if litera in samogloski:
#         licznik_samoglosek += 1
# print(licznik_samoglosek)

# for i in range(5):
#     print(f"fsdgsfsf: {i}")

# a = "#"
# for i in range(6):
#     a += "#"
#     print(a)

# a = int(0)
# for i in range(100):
#     a += 1
#     if a % 15 == 0:
#         print(f"{a} FizzBuzz")
#     elif a % 3 == 0:
#         print(f"{a} Fizz")
#     elif a % 5 == 0:
#         print(f"{a} Buzz")
#     else:
#         print(a)

# zakupy = []
# while True:
#     produkt = input("podaj produkt (lub koniec): ")
#     if produkt.lower() == "koniec":
#         break
#     zakupy.append(produkt)
#     zakupy.sort()
#     print(f"liczba produktow: {len(zakupy)}")
#     for index, produkt in enumerate(zakupy, start = 1):
#         print(f"{index}. {produkt.capitalize()}")

# moja_lista = [1,2,3]
# moja_lista[0] = 99
# print(moja_lista)
# moja_krotka = (1,2,3)
# moja_krotka[0] = 100
# print(moja_krotka)

# lista_z_duplikatami = [1,2,'a',3,'a',True] #True = 1
# unikalne_elmenty = set(lista_z_duplikatami)
# print(unikalne_elmenty)

# slowa = "python, programowanie, python, kurs, nauka, kurs"
# tagi = slowa.split(',')
# for ilosc_tagow in tagi:
#     print(f"liczba tagow:{len(tagi)}")
#     print(f"liczba unikalnych tagow:{len(set(tagi))}")

# osoba = {"imie": "jan",
#          "nazwisko": "kowalski",
#          "wiek": 45
#          }
# print(f"poczatkowy slownik: {osoba}")
# osoba["miasto"] = "warszawa"
# print(f"po dodaniu miasta : {osoba}")
# osoba["wiek"] = 51
# print(f"po zmianie wieku : {osoba}")
# del osoba["nazwisko"]
# print(f"po usunieciu nazwiska : {osoba}")

# kontakty = {}
# print("menu")
# print(f"1. dodaj kontakt lub")
# print(f"2. wyswietl konakt")
# print(f"3. usun kontakt")
# print(f"4. wyswietl wszystko")
# print(f"5. zakoncz")
# while True:
#     a = input("wybierz opcje: ")
#     if a == "1": #dodaj kontakt
#         b = input(f"podaj nazwe: ")
#         c = input(f"podaj numer: ")
#         kontakty[b] = c
#     elif a == "2": #wyswietl kontakt
#         d = input(f"podaj nazwe: ")
#         print(kontakty[d])
#     elif a == "3": #usun kontakt
#         e = input(f"podaj nazwe: ")
#         del kontakty[e]
#     elif a == "4": #wyswietl wszystko
#         print(kontakty)
#     elif a == "5": #zakoncz
#         break
#     else:
#         print("zla komenda")

# kontakty = {
#     "anna": "1234",
#     "piotr": "4321"
# }
# for nazwa in kontakty.keys():
#     print(nazwa)
# for numer in kontakty.values():
#     print(numer)
# for nazwa, numer in kontakty.items():
#     print()

# baza_danych = [
#     {"imie": "anna", "stanowisko": "specjalista", "pensja": "4500"},
#     {"imie": "piotr", "stanowisko": "manager", "pensja": "8000"},
#     {"imie": "zofia", "stanowisko": "specjalista", "pensja": "5200"},
#     {"imie": "krzysztof", "stanowisko": "stazysta", "pensja": "2500"}]
# for ilosc in baza_danych:
#     a = baza_danych[int("pensja")]
#     a+a
#     print(f"{a/baza_danych}")

# def wyswietl_powitanie():
#     print("powitanie")
# wyswietl_powitanie()


# imie = input("podaj imie: ")
# def przywitaj(imie):
#     print(f"witaj: {imie}")
# przywitaj(imie)


# def dodaj(liczba1, liczba2):
#     suma = liczba1 + liczba2
#     return suma
# print(
#     dodaj(
#         int(input("podaj pierwsza liczbe: ")),
#         int(input("podaj druga liczbe: "))
#     ))

# def generuj_raport(imie, stanowisko = "pracownik", miasto = "nieznane"):
#     print(f"imie: {imie}")
#     print(f"stanowisko: {stanowisko}")
#     print(f"miasto: {miasto}")
# generuj_raport(imie = input("podaj imie:"))

# def oblicz_pole(figura = "prostokad", a = 0, h = 0):
#     if(figura.lower() == "prostokad"):
#         wynik = a*h
#         print(wynik)
#     elif(figura.lower() == "kolo"):
#         wynik = math.pi*(h**2)
#         print(wynik)
#     else:
#         print("nie podano figury")
# oblicz_pole(
#     figura = input("podaj figure: "),
#     a = int(input("podaj a: ")),
#     h = int(input("podaj h: ")))

# def generuj_raport(imie, stanowisko = "pracownik", miasto = "nieznane"):
#     return  f" imie: {imie} \n stanowisko: {stanowisko} \n miasto: {miasto}"
# a = generuj_raport(imie = input("podaj imie:"))
# print(a)

# """
# uniwersalny kalkulator pola
#
# args: figura, a, h
# returns: pole figury z a i h
# """
# def oblicz_pole(figura = "prostokad", a = 0, h = 0):
#     if(figura.lower() == "prostokad"):
#         wynik = a*h
#         print(wynik)
#     elif(figura.lower() == "kolo"):
#         wynik = math.pi*(h**2)
#         print(wynik)
#     else:
#         print("nie podano figury")
# oblicz_pole(
#     figura = input("podaj figure: "),
#     a = int(input("podaj a: ")),
#     h = int(input("podaj h: ")))
# help(oblicz_pole())

# def rozdziel_imie_nazwisko(imie_i_nazwisko):
#     return imie_i_nazwisko.split(" ")
# imie, nazwisko = rozdziel_imie_nazwisko("Jan Kowalski")
# print(imie)
# print(nazwisko)

# def zsumuj_wszystko(*liczby):
#     return sum(liczby)
# a = zsumuj_wszystko(1,2,3,4,6)
# print(a)

# def generuj_raport(**szczegoly):
#     for klucz, wartosc in szczegoly.items():
#         print(f"{klucz}: {wartosc}")
# generuj_raport(status = "aktywny", punkty = "150", zalogowany = True)

# def dodaj(a,b):
#     return a+b
# def odejmij(a,b):
#     return a-b
# def wykonaj_operacje(a, b, funkcja_operacji):
#     return funkcja_operacji(a,b)
# print(wykonaj_operacje(5,4,dodaj))
# print(wykonaj_operacje(5,4,odejmij))

# x = "globalny"
# def funkcja_zewnetrzna():
#     x = "otaczajacy"
#     def funkcja_wewnetrzna():
#         x = "lokalny"
#         print(x)
#     funkcja_wewnetrzna()
#     print(x)
# funkcja_zewnetrzna()
# print(x)

# licznik = 10
# def proba_modyfikacji():
#     licznik = 20
#     print(f"wewnatrz funkcji: {licznik}")
# proba_modyfikacji()
# print(f"na zewnatrz funkcji: {licznik}")

# licznik_globalny = 100
# def funkcaj_zewnetrzna():
#     licznik_enclosing = 50
#     def funkcja_wewnetrzna():
#         global licznik_globalny
#         nonlocal licznik_enclosing
#         licznik_globalny +=1
#         licznik_enclosing += 1
#         print(f"wew global: {licznik_globalny} enclosing: {licznik_enclosing}")
#     funkcja_wewnetrzna()
#     print(f"zew global: {licznik_globalny} enclosing: {licznik_enclosing}")
# funkcaj_zewnetrzna()

# def funkcji(a, b, c):
#     print(f"a= {a}, b= {b}, c= {c}")
# lista_arg = [10, 20, 30]
# slownik_arg = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
# funkcji(*lista_arg)
# funkcji(**slownik_arg)

# def wyslij_email(adres, temat, *, priorytet = "normalny"):
#     print(f" adres: {adres} \n temat: {temat} \n priorytet: {priorytet}")
# wyslij_email("wefw", "byjk", priorytet="nienormalny")

# def moj_dekorator(funkcja_do_udekorowania):
#     def wrapper():
#         print("cos przed wywolaniem funkcji")
#         funkcja_do_udekorowania()
#         print("cos po wywolaniu funkcji")
#     return wrapper
# @moj_dekorator
# def powiedz_czesc():
#     print("czesc")
# powiedz_czesc()

# def uniwersalny_dekorator(funkcja):
#     @functools.wraps(funkcja)
#     def wrapper(*args, **kwargs):
#         print("cos przed")
#         wynik = funkcja(*args, **kwargs)
#         print("cos po")
#         return wynik
#     return wrapper
# @uniwersalny_dekorator
# def dodaj(a, b):
#     return a + b
# rezultat = dodaj(10 ,5)

# def mierz_czas(funkcja):
#     @functools.wraps(funkcja)
#     def wrapper(*args, **kwargs):
#         przed = time.time()
#         wynik = funkcja(*args, **kwargs)
#         po = time.time()
#         roznica = po - przed
#         return wynik, roznica
#     return wrapper
# @mierz_czas
# def dodaj(a, b):
#     time.sleep(1)
#     return a + b
# rezultat = dodaj(10 ,5)
# print(f"rezultat: {rezultat[0]}, czas wykonania: {rezultat[1]:.4f}")

# def prosty_generator():
#     print("zaraz zwroce pierwsza wartosc")
#     yield "pierwsza wartosc"
#     print("zaraz zwroce druga wartosc")
#     yield  "druga wartosc"
# gen = prosty_generator()
# print(next(gen))
# print(next(gen))

# def licz_do_trzech():
#     print("generator wznawia prace")
#     yield 1
#     print("generator wznawia prace")
#     yield 2
#     print("generator wznawia prace")
#     yield 3
#     print("generator konczy prace")
# gen = licz_do_trzech()
# print("zaczyna iterowac po generatorze: ")
# for i in gen:
#     print(i)

# def fibonacci(limit):
#     a = 0
#     b = 1
#     for _ in range(limit):
#         yield a
#         a, b = b, a + b
# for liczba in fibonacci(10):
#     print(liczba)

# liczby = [1,2,3]
# kwadraty = list(map(lambda x: x**2, liczby))
# print(kwadraty)

# liczby = [1,2,3,4]
# parzyste = list(filter(lambda x: x%2 == 0, liczby))
# print(parzyste)

# imiona = ["anna", "piotr", "zofia"]
# nowe = list(map(lambda imie: imie.capitalize(),imiona))
# print(nowe)
# oceny = [5,3,2,5,4,2,3,4]
# nowe2 = list(filter(lambda ocena: ocena >= 4, oceny))
# print(nowe2)

# def sprawdz_typy(typ_argumentu):
#     @functools.wraps(typ_argumentu)
#     def wrapper(*args, **kwargs):
#         for _ in args:
#             wynik = typ_argumentu(isinstance(*args, int), **kwargs)
#         return wynik
#     return wrapper
# @sprawdz_typy(int)
# def dodaj(a, b):
#     return a + b
# rezultat = dodaj(10 ,5)
# print(rezultat)

# import narzedzia
# narzedzia.przywitaj("jan")

# from narzedzia import przywitaj
# przywitaj("jan")

# import narzedzia
# @narzedzia.mierz_czas
# def wolna_funkcja():
#     time.sleep(2)
#     print("dsgsdg")
# wolna_funkcja()

# from narzedzia_firmowe.pomiar import mierz_czas
# from narzedzia_firmowe.formatowanie import na_wielkie_litery
# @mierz_czas
# def wolna_funkcja():
#     time.sleep(2)
#     print("dsgsdg")
# wolna_funkcja()
# print(na_wielkie_litery("\ntekst"))

# produkty = [
#     {"nazwa" : "rower", "cena" : 999.99},
#     {"nazwa" : "pilka", "cena" : 2.50},
#     {"nazwa" : "worek_ziemniakow", "cena" : 50}
# ]
# posortowane_produkty = sorted(produkty, key=lambda p:p["cena"])
# print(posortowane_produkty)

# oceny = [1,5,3,4,2]
# czy_jest_zagrozenie = any(x < 3 for x in oceny)
# print(f"czy jest zagrozenie: {czy_jest_zagrozenie}")
# czy_wszystkie_pozytywne = all(x >= 3 for x in oceny)
# print(f"czy wszystkie pozywywne: {czy_wszystkie_pozytywne}")

from functools import reduce
liczby = [5,2,8,1,9]
najwieksza = reduce(lambda a,b: a if a > b else b, liczby)
print(najwieksza)
