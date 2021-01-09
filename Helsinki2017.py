#Név         ;Ország    ;Technikai   ;Komponens   ;Levonás
#Zijun LI    ;CHN       ;53.96       ;49.54       ;0


f = open("rovidprogram.csv")
f0 = open("donto.csv")

f.readline()
f0.readline()

elsoresz = [sor.strip().split(';') for sor in f]
masodikresz = [sor.strip().split(';') for sor in f0]

print(f"2. Feladat: {len(elsoresz)} versenyző adott elő rövidprogramot")