import random


def oyun_oyna():
    gizli_sayi = random.randint(1, 100)
    maksimum_hak = 7
    deneme_sayisi = 0

    print("\n1 ile 100 arasında bir sayı tuttum.")
    print(f"{maksimum_hak} tahmin hakkın var.")

    while deneme_sayisi < maksimum_hak:
        try:
            tahmin = int(input("\nTahminin: "))
        except ValueError:
            print("Lütfen sadece sayı gir.")
            continue

        if tahmin < 1 or tahmin > 100:
            print("Lütfen 1 ile 100 arasında bir sayı gir.")
            continue

        deneme_sayisi += 1
        kalan_hak = maksimum_hak - deneme_sayisi

        if tahmin < gizli_sayi:
            print("Daha büyük bir sayı dene.")

        elif tahmin > gizli_sayi:
            print("Daha küçük bir sayı dene.")

        else:
            print(f"\nTebrikler! Sayıyı {deneme_sayisi}. denemede bildin.")
            return

        if kalan_hak > 0:
            print(f"Kalan hakkın: {kalan_hak}")

    print(f"\nTahmin hakkın bitti. Doğru cevap {gizli_sayi} idi.")


print("Sayı Tahmin Oyununa Hoş Geldin!")

while True:
    oyun_oyna()

    tekrar = input("\nTekrar oynamak ister misin? (e/h): ").lower()

    if tekrar != "e":
        print("Oyunu oynadığın için teşekkürler.")
        break