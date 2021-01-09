#Név         ;Ország    ;Technikai   ;Komponens   ;Levonás
#Zijun LI    ;CHN       ;53.96       ;49.54       ;0


f = open("rovidprogram.csv")
f0 = open("donto.csv")

f.readline()
f0.readline()

elsoresz = [sor.strip().split(';') for sor in f]
masodikresz = [sor.strip().split(';') for sor in f0]

print(f"2. Feladat: {len(elsoresz)} versenyző adott elő rövidprogramot")

bejutott = False
for sor in masodikresz:
    if sor[1] == "HUN":
         bejutott = True

if bejutott:
    print("3.Feladat: Bejutott magyar versenyző a kürtbe")
else:
    print("3.Feladat: Nem jutott be magyar versenyző a kürtbe")


