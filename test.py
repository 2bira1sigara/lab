try:
    x = int(input("ilk sayi gir: " ))
    y = int(input("ikinci sayi gir: "))
    z = int(input("ucuncu sayi gir: "))
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    elif z > x and z > y:
        print(z)
    else:
        print(" ayni olmasin irzini siktigim")

except:
    print("Gecersiz input")

