import time
import functools


def mierz_czas(funkcja):
    functools.wraps(funkcja)

    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        koniec = time.time()
        roznica = koniec - start
        return wynik, roznica

    return wrapper


@mierz_czas
def dodaj(a, b):
    return a + b


@mierz_czas
def przywitaj(x):
    return f"Witaj {x}"


funk1 = dodaj(1, 2)
funk2 = przywitaj("Bartek")

print(f"Rezultat: {funk1[0]}, w czasie {funk1[1]:.4f}")
print(f"Rezultat: {funk2[0]}, w czasie {funk2[1]:.4f}")
