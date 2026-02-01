import pickle

class StanGry:
    def __init__(self, nazwa_gracza: str, punkty: int, ekwipunek: list):
        self.nazwa_gracza = nazwa_gracza
        self.punkty = punkty
        self.ekwipunek = ekwipunek

    def __repr__(self):
        return f"StanGry(nazwa_gracza={self.nazwa_gracza}, punkty={self.punkty}, ekwipunek={self.ekwipunek})"

stan_gry = StanGry(nazwa_gracza="Player1", punkty=1500, ekwipunek=["miecz", "tarcz", "zbroja"])

with open("stan_gry.pkl", "wb") as f:
    pickle.dump(stan_gry, f)

with open("stan_gry.pkl", "rb") as f:
    wczytany_stan = pickle.load(f)

print(wczytany_stan)
print(type(wczytany_stan))
