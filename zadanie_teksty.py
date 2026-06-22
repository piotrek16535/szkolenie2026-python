from datetime import datetime, date, timedelta
tekst_CSV="03/22/2025 jan KOWalski wypłata PLN: 8359"

rok=tekst_CSV[6:10]
miesiac=tekst_CSV[0:2]
dzien=tekst_CSV[3:5]
print(f"Rok: {rok}\nMiesiąc: {miesiac}\nDzień: {dzien}")
a=tekst_CSV.find("wypłata")
#print(a)
Imie_nazwisko=tekst_CSV[11:a]
Imie_nazwisko=Imie_nazwisko.lower()
print(Imie_nazwisko.title())
b=tekst_CSV.find("PLN")
c=b+4
wyplata=tekst_CSV[c:]
print(wyplata)
wypłataEuro=float(wyplata)/4.33
print(f"{wypłataEuro:.2f}")
nowa_wyplata=10999.76
nowe_dane=tekst_CSV.replace("jan","marek").replace("KOWalski","piEKNY").replace(str(wyplata),str(nowa_wyplata))
print(nowe_dane)
data=date(int(rok),int(miesiac),int(dzien))
szkolenie=data+timedelta(days=270)
print("Szkolenie dnia:",szkolenie)
lista=tekst_CSV.split()
print(lista)
#lista.append([1000, 15000])
#print(lista)
lista.extend([1000, 15000])
print(lista)