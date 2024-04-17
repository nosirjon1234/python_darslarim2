#royxat bilan islash
mevalar = ["olma", "gilos", "shaftoli", "nok"]
#mevalar.sort()# sotr metodi royxxatdagi elemantlarni birinchi haarflariga qarab alifbo ketma ketligida qilib beradii
#mevalar.sort(reverse=True)# .sort(reverse=True metodi elemantlarni birinchi haarflariga qarab alifboni teskarisiga qarab qiberadi
#mevalar.reverse()# .reverse metodi elementlarni teskarisiga qilib beradi
len(mevalar)# len() royxat ichidagi elementlarni sanaydi
print(mevalar)

sonlar = [12 ,23,35,446,81,32,231213,5465,5654,]

#sonlar.sort(reverse=True)# bu metodlar sonlarda ham ishllaydi
#sonlar.sort()# bu metodlar sonlarda ham ishllaydi\
sonlar.reverse()# .reverse metodi elementlarni teskarisiga qilib beradi
print(sonlar)

#son = list(range(0,11))# sonlar oraligini sanaydi
son = list(range(1,20,2))# bunda toq sonlarlar chiqadi 1 bu boshlangih, 20 tugash soni, 2 bu 2ta tashab sanash belgisi
print(son)

max = max(sonlar)
narx = min(sonlar)
jami = sum(sonlar)
print("eng arzon narx", narx, "eng qimmat narx",  max, "jami ", jami)

print(mevalar[0:3])# bunda bir necha qiymatni royxatdan sugurib olish

fruet = mevalar[:]# bu mevalar degan royxatdagi elementlarni nusxaa olib fruet royxat ichiga qoyyapdi

fruet.append("orik")
print(fruet)
print(mevalar)

toys = ("bus", "egd",)# tuple royxat bu buni ozgartirib bolmaydi
print(type(toys))