class Gracz:
    liczba_graczy = 0

    def __init__(self,hp,nick):
        self._hp = hp
        self.nazwa = nick
        Gracz.liczba_graczy += 1
        self.ekwipunek = Ekwipunek()

    def __str__(self):
        return f"Twoja nazwa: {self.nazwa}, twoje hp: {self.hp} "

    def pokaz_status(self):
        print(f"Twoja nazwa: {self.nazwa},\n"
              f"twoje hp : {self.hp}")

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,nowa_wart):
        if nowa_wart <= 0:
            self._hp = 0
        else:
            self._hp = nowa_wart

    def otrzymaj_obrazenia(self,ilosc):
        self.hp = self.hp - ilosc
        print(f"{self.nazwa} otrzymałes {ilosc} obrazen, twoje hp po : {self.hp}")

class Wojownik(Gracz):
    def __init__(self,hp,nick,sila):
        super().__init__(hp,nick)
        self.sila = sila

    def pokaz_status(self):
        super().pokaz_status()
        print(f"twoja siła : {self.sila}")

    def atak(self):
        print(f"{self.nazwa} atakuje z sila {self.sila}")

class Mag(Gracz):
    def __init__(self,hp,nick,mana):
        super().__init__(hp,nick)
        self.mana = mana

    def pokaz_status(self):
        super().pokaz_status()
        print(f"twoja mana : {self.mana}")

    def atak(self):
        print(f"{self.nazwa} atakuje z i traci {self.mana} pkt. many")

class Ekwipunek:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self,item):
        self.przedmioty.append(item)

    def pokaz_przedmioty(self):
        print(self.przedmioty)

gracz1 = Gracz(100,"piernik")
wojownik1 = Wojownik(100,"kot",12)
mag1 = Mag(100,"czarodziej pies",120)

wojownik1.ekwipunek.dodaj_przedmiot("miecz")
wojownik1.ekwipunek.dodaj_przedmiot("zbroja")
wojownik1.ekwipunek.dodaj_przedmiot("topór")

wojownik1.ekwipunek.pokaz_przedmioty()

gracz1.hp = -123
druzyna = [gracz1,wojownik1,mag1]
