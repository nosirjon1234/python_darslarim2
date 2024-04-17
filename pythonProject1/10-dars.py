#if elif else


#yosh = int(input("Yoshingizni kiriting:"))
#if yosh<=10:
#    narx = "bepul"
#elif yosh<=25:# aks holda
#    narx = 10000
#elif yosh<=45:
#    narx = 15000
#else:
#    narx = "bepul"


#print(f"sizga kirish {narx} somda")

#kun = input("Bugun nima kunda?")
#if  kun.lower() == "shanba" or kun.lower() == "yakshanba":# or aperatori yoki degan manoda keladi
#    print("Bugun dam olish kuni")
#else:
#    print("Bugun ish kuni")

day = input("Bugun nima kunga?")
harorart = int(input("Harorat nechi gradus?"))

if day.lower()=="yakshanba" or day.lower()=="shanba" and harorart>=30:# and va ornida kelyapti
    print("Chomilgani ketdik")
elif  day.lower()=="yakshnba" or day.lower()=="shanba" and harorart<=30:
    print("Uyda dam olamiz")


narh = 15000
choy = True
salat = False
non = True
yog = True
gosht = False

if choy:
    print("Mijoz choy oldi.")
    narh = narh +3000
if salat:
    print("Mijoz salat oldi")
    narh = narh + 5000
if non:
    print("Mijoz non oldi")
    narh = narh + 3000
if yog:
    print("Mijoz yog oldi.")
    narh = narh + 10000
if gosht:
    print("Mijoz gosht oldi.")
    narh = narh + 750000
print(f"Jami summa {narh} som")




#if choy and salat:
#    narh = narh + 10000
#elif choy or salat:
#    narh = narh + 5000

#print(f"Jami narh {narh} som")



menu = ["somsa","manti","dimlama","osh","grill"]
ovqat = input("Nima ovqat yiysiz?")
if ovqat.lower() in menu:# in bu borligini tekshirish operatori
    print("Buyurtma qabul qilindi")
else:
    print("Afsuski bizda bunday ovqat yoq")

print(menu)

menu2 = ["somsa","manti","dimlama","osh","grill"]
if ovqat.lower() not in menu:# not in bu yoqligini tekshirish operatori
    print("Buyurtma qabul qilindi")
else:
    print("Afsuski bizda bunday ovqat yoq")

print(menu2)



menu2 = ["somsa","manti","dimlama","osh","grill"]
buyurtmalar = ["somsa","manti","dimlama","shashlik"]

if buyurtmalar:
    for toam in buyurtmalar:
        if toam in menu:
            print(f"Menuda {toam} bor")
        else:
             print(f"Afsuski Menuda {toam} yoq")
else:
    print("Savatchangiz bosh")

