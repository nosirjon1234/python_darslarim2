#Lugat


cars = {"model":"BMW M3", "rang":"qora"}
print(f"Moshina modeli {cars['model']} rangi {cars['rang']}")


# yangi  kalit va qiymat qoshish
cars['Mercedes-Benz'] = 'G-класс'
cars['rangi'] = 'qizil'

print(cars)

mevalar = {"olma":10000, "banan":12000, "qovun":8000}
for meva in mevalar:
    print(f"{meva.capitalize()} narxi {mevalar[meva]} som")


mevalar['shaftoli'] = 7000


#Lugatlarni bir nechta qatorda yozish

telefonlar = {
    'ali':'Iphone 15',
    'vali':'Iphone 14',
    'hasan':'Iphone 13',
    'husan':'Iphone 12'
}
print()

# get () metodi - lugatdan biron malumotni olish
# get() metodidan fodalansak bizga 2 qiymat beradi 1-lugatdagi kalit soz 2-kalit sozga mos keluvchi qiymat yoq bolsa aytuvhi habar
telefon = telefonlar.get("ali", "Bunday ism mavjud emas")
print(telefon)

#agarda biz get() metodini ishlatganimizda 2-qiymatni yozmasak bizga kalit sozga mos qiymat chiqmasa none degan habar beradi
#none degani bu mavjud emas

phone = telefonlar.get("olim")
print(phone)