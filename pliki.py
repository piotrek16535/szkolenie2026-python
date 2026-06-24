# 1 otwarcie pliku
plik=open(r"C:\Users\Szkolenie_03\Desktop\Szkolenie\szkolenie2026-python\dane_tekstowe.txt","rt",encoding="utf8")
zawartosc=plik.read()
print(zawartosc)
#restart kursora na początku
plik.seek(0)
i=0
for wiersz in plik:
    i+=1
    print("WIERSZ ", i, "=", wiersz)
#zamykanie pliku
plik.close()

with open(r"C:\Users\Szkolenie_03\Desktop\Szkolenie\szkolenie2026-python\dane_tekstowe.txt","rt",encoding="utf-8") as plik:

    plik.write("\nNowy tekst")
    
#with open(r"C:\Users\Szkolenie_03\Desktop\Szkolenie\szkolenie2026-python\dane_tekstowe.txt","rt",encoding="utf-8") as plik:

 #   for linia in plik:
#        print(linia.strip())
