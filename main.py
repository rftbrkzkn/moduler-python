from hesaplama.toplama import topla
from hesaplama.cikarma import cikar

def main():
    a = 10
    b = 5
    print(f"Toplam: {topla(a, b)}")
    print(f"Fark: {cikar(a, b)}")

if __name__ == "__main__":
    main()
