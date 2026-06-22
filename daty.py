from datetime import datetime, date, timedelta
teraz=datetime.now()
print(f"Teraz jest: {teraz}")
print("Teraz jest:",teraz)

urodziny=date(1995,10,14)
print(f"Urodziny:{urodziny}")

przyszlosc=teraz+timedelta(days=100)
print(f"Za 100 dni będzie: {przyszlosc.date()}")

dzisiaj=datetime.now()
print(f"rok: {dzisiaj.year}")
#Obiekt -> Tekst
ladna_data=teraz.strftime("%d.%m.%Y %H:%M")
print(f"Format europejski: {ladna_data}")
#Tekst -> Obiekt 
data_z_pliku="2026-12-31"
obiekt_daty=datetime.strptime(data_z_pliku, "%Y-%B-%d")
print(f"Data: {obiekt_daty}")