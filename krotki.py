mieszana =("Ania",24,True)
#mieszana[0]="Zosia"
print(mieszana)
k=len(mieszana)
print(k)

k1=(1,2)
k2=(3,4)
wynik=k1+k2
print(wynik)
print(2 in wynik)
lista=list(mieszana)
lista[0]="nowy"
mieszana=tuple(lista)
print(mieszana)