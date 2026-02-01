import json
from pydantic import BaseModel, ValidationError

class SpecyfikacjaModel(BaseModel):
    procesor: str
    ram_gb: int

class ProduktModel(BaseModel):
    nazwa_produktu: str
    id_produktu: str
    cena: float
    dostepny: bool
    tagi: list[str]
    specyfikacja: SpecyfikacjaModel

def wczytaj_i_waliduj_produkt(sciezka: str) -> ProduktModel | None:
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            dane = json.load(f)
        produkt = ProduktModel.parse_obj(dane)

        return produkt

    except FileNotFoundError:
        print("Plik nie został znaleziony.")
        return None

    except json.JSONDecodeError:
        print("Błąd formatu JSON.")
        return None

    except ValidationError as e:
        print("Błąd walidacji danych:")
        print(e)
        return None
produkt = wczytaj_i_waliduj_produkt("produkt.json")

if produkt:
    print("Produkt został poprawnie wczytany")
    print("Nazwa produktu:", produkt.nazwa_produktu)
    print("Procesor:", produkt.specyfikacja.procesor)
    print("RAM (GB):", produkt.specyfikacja.ram_gb)
