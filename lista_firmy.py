from tkinter import messagebox
# 1. wersja
firmy = ["Firma 1","Firma 2","Firma 3","Firma 4","Firma 5","Firma 6","Firma 7"]
Kurs_akcji_wczoraj = [16.48, 25.24,57.23,37.92,99.59,94.39,91.56]  
Kurs_akcji_dzis    = [16.71,25.64 ,57.11, 38.16, 99.14, 94.52, 91.11]
komunikat_mb=""
ile=len(firmy)
for i in range(ile):
    firma=firmy[i]
    kurs_w=Kurs_akcji_wczoraj[i]
    kurs_d=Kurs_akcji_dzis[i]
    wynik=round(kurs_d-kurs_w,2)
    if wynik<0:
        info="spadł"
    else:
        info="wzrósł"
    tekst=f'Firma: {firma}, kurs akcji {info} o {wynik}'
    komunikat_mb+=tekst+'\n'


messagebox.showinfo("Informacja",komunikat_mb)
""""
# 2. wersja
firmy = {}
firmy["Nazwa firmy"] = ["Firma 1","Firma 2","Firma 3","Firma 4","Firma 5","Firma 6","Firma 7"]
firmy["Kurs akcji wczoraj"] = [16.48, 25.24,57.23,37.92,99.59,94.39,91.56]  
firmy["Kurs akcji dziś"] = [ 16.71,25.64 ,57.11, 38.16, 99.14, 94.52, 91.11  ]
firmy["Wzrost/Spadek"]=[None,None,None,None,None,None,None]
firmy["Wartość"]=[None,None,None,None,None,None,None]
"""
