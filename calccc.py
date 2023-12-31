def hesapla(a, b, islem):
    if islem == "+":
        return str(a) + " + " + str(b) + " = " + str(a + b)
    elif islem == "-":
        return str(a) + " - " + str(b) + " = " + str(a - b)
    elif islem == "*":
        return str(a) + " * " + str(b) + " = " + str(a * b)
    elif islem == "/":
        return str(a) + " / " + str(b) + " = " + str(a / b)
    else:
        return "Geçersiz işlem!"
while True:
    try:
        a = int(input("Lütfen İlk Sayiyi Giriniz: "))
        b = int(input("Lütfen İkinci Sayiyi Giriniz: "))
        islem = input("Lütfen yapmak istediğiniz işlemi giriniz: +, -, *, / ")
    except:
        print("Lütfen sayilari düzgün giriniz!")
    
    sonuc = hesapla(a, b, islem)
    print(sonuc)
