def string_to_double(s):
    try:
        double_değer = float(s)
        return double_değer
    except ValueError:
        return None

if __name__ == "__main__":
    # Programın açıklaması
    print("Bu program bir string'i double (ondalık sayıya) dönüştürür.")
    print("'q' tuşuna basarak çıkabilirsiniz.")

    while True:
        # Kullanıcıdan giriş al
        string_değer = input("Lütfen bir sayı girin: ")

        # Çıkış kontrolü
        if string_değer.lower() == 'q':
            print("Programdan çıkılıyor...")
            break

        # String'i double'a dönüştür
        double_değer = string_to_double(string_değer)

        if double_değer is not None:
            print("Double değeri:", double_değer)
        else:
            print("Geçersiz giriş! Lütfen bir sayı girin.")