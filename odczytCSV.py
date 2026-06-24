import csv

with open(r"C:\Users\Szkolenie_03\Desktop\Szkolenie\szkolenie2026-python\dane.csv" ,mode='r',encoding='utf-8') as plik:
    czytnik =csv.DictReader(plik,delimiter=';')

    for wiersz in czytnik:
        print(f"Pojazd: {wiersz['Marka pojazdu']}, Cena: {wiersz['Cena netto']}")