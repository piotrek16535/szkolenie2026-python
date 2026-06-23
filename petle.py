cars=['audi','bmw','skoda','kia']
garaz={
    "Toyota" : "Corolla",
    "Mazda" : "CX-5",
    "BMW" : "M3",
    "Tesla" : "Model 5"
}
print("Opcja 1")
for car in cars:
    print("Pojazd: ",car)

print("Opcja 2")
#alternatywa
ile_razy=len(cars)
for element in range(ile_razy):
    print(f'pokazuje element: {element} tablicy o wartości: {cars[element]}')

print("Opcja 3")
#3 opcja
for ile, car in enumerate(cars,start=0):
    print("Pojazd nr =",ile,end=' ')
    print("to: ",car)

print("\n-------MOJA KOLEKJA----------")
for marka, model in garaz.items():
    print(f"Marka: {marka} | Model: {model}")

print("\n-------POSIADANE MARKI----------")
for marka in garaz.keys():
    print(f"Mam w garażu marki: {marka}")
    pojazd=garaz[marka]

print("\n-------MOJE MARKI----------")
for model in garaz.values():
    print(f"Mam w garażu pojazd: {model}")

auta_szczegoly={
    "WA12345": {"marka": "Toyota", "rok":2020, "przebieg": 50000},
    "KR56789": {"marka": "BMW", "rok":2018, "przebieg": 120000}
}

for rejestracja,dane in auta_szczegoly.items():
    print(f"Auto o numerze {rejestracja}:")

    marka = dane["marka"]
    rok = dane["rok"]
    przebieg = dane["przebieg"]

    print(f" -> {marka} z roku {rok} ma przebieg: {przebieg}")