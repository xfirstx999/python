import functools
import time

def mierz_czas(funkcja):
    @functools.wraps(funkcja)
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        koniec = time.time()
        roznica = koniec - start
        print(f"czas wykonania: {roznica:.4f}")
        return wynik
    return wrapper

if __name__ == "__main__":
    print("askdjasdk")