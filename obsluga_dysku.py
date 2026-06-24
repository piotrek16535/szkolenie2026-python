import os

sciezka_do_pliku=os.path.join("dane","tajny_plik.txt")
if os.path.exists(sciezka_do_pliku):
    os.remove(sciezka_do_pliku)
    print("Plik bezpiecznie usunieto.")
else:
    print("Spokojnie, pliku juz nie ma")


folder_wynikowy=r"C:\Users\Szkolenie_03\Desktop\Szkolenie\lokalizacje"
if not os.path.exists(folder_wynikowy):
    os.makedirs(folder_wynikowy)