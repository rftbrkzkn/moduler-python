from hesaplama.toplama import topla
from hesaplama.cikarma import cikar
from hesaplama.carpma import carp
from hesaplama.bolme import bolme
def main():
    a = 10
    b = 5
    print(f"Toplam: {topla(a, b)}")
    print(f"Fark: {cikar(a, b)}")
    print(f"Carpim: {carp(a,b)}")
    print(f"Bolum: {bolme(a,b)}")

if __name__ == "__main__":
    main()
