dict={
    "brand":"Ford",
    "model":"Mondeo",
    "year": 2018
}
print(dict)

y=dict.get("model_auta", "brak danych")
print(y)
dict["year"]=2023
dict["kolor"]="czarny"
x=dict["year"]
print(x)
z=dict["kolor"]
print(z)

mapa={
    (52.2,21.0):"Warszawa"
}
print(mapa)
mapa.clear()
print(mapa)