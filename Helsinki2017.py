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


def OsszPontszam(versenyzo):
    pontszam = 0.0
    for sor in elsoresz:
        if sor[0] == versenyzo:
            pontszam = pontszam + float(sor[2])
            pontszam = pontszam + float(sor[3])
            pontszam = pontszam - float(sor[4])
    for sor in masodikresz:
        if sor[0] == versenyzo:
            pontszam = pontszam + float(sor[2])
            pontszam = pontszam + float(sor[3])
            pontszam = pontszam - float(sor[4])
    return pontszam


versenyzo = input("5.Feladat: Kérem a versenyző nevét ")
resztvett = False
for sor in elsoresz:
    if (sor[0] != versenyzo):
        reszvett = True
if reszvett:
    print("Ilyen nevű induló nem volt")
else:
    print(f"6.Feladat:A versenyző összpontszáma: {OsszPontszam(versenyzo)}")