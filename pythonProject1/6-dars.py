#List

mevalar = ["olma", "orik", "shaftoli", "nok"]
narxlar = [12000, 12500, 13000, 14000]
sonlar = ["bir", "ikki", 3, 4, 5]
cars = []

print(mevalar[0].capitalize())
print(mevalar[1].capitalize())
print(mevalar[-2].capitalize())
print(mevalar[-1].capitalize())
mevalar[0] = "nok"
print(mevalar)
mevalar.append('gilos')#.insert metodi yordamida royxatni ohriga  malumot kiritish mumukin
mevalar.insert(0, 'olma')#.insert metodi yordamida royxatni hohlagan joyig malumot kiritish mumukin
print(mevalar)

cars.append("nexia")
cars.append("malibu")
cars.append("gentra")
cars.append("lacetti")
cars.append("spark")
cars.append("damaz")

del cars[2]# del indexga qaeab ochiradii
cars.remove("lacetti")# .remove qiymatiga qarab royxatdan ochirib tashlaydi

print(cars)

hayvonlar = ["it", "mushuk", "ot", "baliq", "mushuk"]
hayvonlar.remove("mushuk")# agarda bitta royxatda kop marotoba kelgan qiymatlarni faqat birinchisini ochirib tashlaydi
print(hayvonlar)

bozorlik = ["yog", "un", "olma", "banan", "gosht"]
mahsulot = bozorlik.pop(3)# pop metodi royxatdagi qiymatlarni indexga qarab sugurib oladi index qoyilmasa ohirdagi qiymatni oladi 
print("Men sotib olgan mahsulot: " + mahsulot)
print("Olinmagan mahsulotlar: ",  bozorlik)