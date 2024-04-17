#if else


cars = ["audio", "bmw","nexia","giguli"]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
       print(car.title())


ism = input("Ismingizni kiriting: ")
if ism.lower() != "ali":
    print(f"Uzr, {ism.title()} biz Alini kutyapmiz")

else:
    print("Salom, Ali")


javob = float(input("12x6 nechiga teng: "))
if javob!=72:
    print("Javob xato:")
else:
    print("Javob togri:")

login = input("Loginingizni kiriting")
if len(login)<=5:
    print("Login 5ta son yoki harfdan koproq bolishi kerak")
else:
    print("Xush kelibsiz")

name = int(input("Yoshingizni kiriting"))
if name>=18:
    print("Xsuh kelibsiz")
else:
    print("Kirishingiz mumkin emas")

yil = int(input("Yilingizni kiriting:"))
if 2024-yil<18:
    print("Siz {2024-yil} yoshda ekansiz.")
    print("Sizning kirishingiz mumkin emas")
else:
    print("Xush kelibsiz")