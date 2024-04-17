#tsikl


mehmonlar = ["ali", "vali", "hasan", "husan"]

for mehmon in mehmonlar:
    print("salom", mehmon.capitalize() )




sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)


print(sonlar)
print(sonlar_kvadrati)

dostlar = []

print("3 eng yaqin dostingizni ismini kiriting")
for a in range(3):
    dostlar.append(input(f"{a+1}-dostingizni ismini kiriting: ").capitalize())
print(dostlar)