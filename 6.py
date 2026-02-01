import functools


def sprawdz_typy(typ_argumentu):
    @functools.wraps(typ_argumentu)
    def wrapper(*args, **kwargs):
        for i in args:
            wynik = typ_argumentu(isinstance(*args, int), **kwargs)
        return wynik

    return wrapper


@sprawdz_typy(int)
def dodaj(x, y):
    return x + y


rezultat = dodaj(1, 2)
print(rezultat)
