from prettytable import PrettyTable as pt, SINGLE_BORDER
#pomocnicze zmienne
pojazdy={}
#tbl = pt()
#tbl.set_style(SINGLE_BORDER)
#tbl.field_names=(["Marka","Ile","Suma","Śr.przebieg"])

#odczyt
with open(r"C:\Users\Szkolenie_03\Desktop\Szkolenie\szkolenie2026-python\dane.csv","rt",encoding="utf-8") as plik:

# odczytanie 1 wierza i przesuniecie kursora na wiersz 2

    naglowki=plik.readline()

 
#odczyt danych wiersz po wierszu
    for wiersz in plik:
      lista_rekord=wiersz.strip().split(";")
      marka=lista_rekord[1]
      lokalizacja=lista_rekord[7]

      if lokalizacja not in pojazdy:
          pojazdy[lokalizacja]={}
        
      if marka not in pojazdy[lokalizacja]:
          pojazdy[lokalizacja][marka]={"suma_cen":0,"Śr.Przebieg":0,"ile":0}

      pojazdy[lokalizacja][marka]["ile"]+=1
      pojazdy[lokalizacja][marka]["suma_cen"]+=int(lista_rekord[2])
      pojazdy[lokalizacja][marka]["Śr.Przebieg"]+=int(lista_rekord[8])
#dodanie wierszy
  #  for m in pojazdy.keys():
   #     tbl.add_row( [m, pojazdy[m]] )


for lokalizacja,marka in pojazdy.items():
    tbl = pt()
    tbl.set_style(SINGLE_BORDER)
    tbl.field_names=(["Marka","ile","Suma","Śr.Przebieg"])
    for m in pojazdy[lokalizacja].keys():
        pojazdy[lokalizacja][m]["Śr.Przebieg"]=round(pojazdy[lokalizacja][m]['Śr.Przebieg'] / pojazdy[lokalizacja][m]["ile"],2)

        tbl.add_row([m,pojazdy[lokalizacja][m]["ile"],
                       pojazdy[lokalizacja][m]["suma_cen"],
                       pojazdy[lokalizacja][m]["Śr.Przebieg"]
                    ])
    nazwa_pliku="dane_"+lokalizacja+".csv"
    with open(nazwa_pliku,'w',encoding='utf8',newline="") as plik:
        plik.write("----------------- dane z PrettyTable\n")
        plik.write(str(tbl))
        plik.write("\n----------------- dane z PrettyTable JAKO CSV\n")
        plik.write(tbl.get_csv_string())
    #print(lista_rekord)

# nie zamykam pliku, sam się zamknie


# zapisz w kolejnym nowym pliku informacje o sumie cen marki pojazdu
liczba=str(-12.5)
if len(liczba)<8:
    print(liczba.ljust(8,"0"))

# Przygotuj tyle plikó ile województw, zapisz obliczenia