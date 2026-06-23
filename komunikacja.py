from tkinter import simpledialog
from tkinter import messagebox
from prettytable import PrettyTable, MSWORD_FRIENDLY, PLAIN_COLUMNS

tabela=PrettyTable()
tabela.set_style(MSWORD_FRIENDLY)
tabela.field_names=["Samochód","rabat"]

tabela.add_row(["opel",0.15])
tabela.add_row(["skoda",0.18])
tabela.add_row(["audi",0.2])

print(tabela)

cena=simpledialog.askinteger("cena","Podaj cenę pojazdu", minvalue=0, maxvalue=500000)

pojazd =simpledialog.askstring("pojazd","Podaj markę pojazdu:")
pojazd=pojazd.lower()
if pojazd=="":
    messagebox.showinfo("Info","Nie podano marki!")
    exit()
if pojazd=="opel":
    rabat=0.15
elif pojazd=="skoda":
    rabat=0.18
elif pojazd=="audi":
    rabat=0.2
else:
    rabat=0.05

cena_rabat=round((int(cena)*(1-rabat)),2)
print("Cena pojazdu ", cena_rabat, "PLN")

odpowiedz = messagebox.askyesnocancel("Wyjście", "Czy na pewno chcesz zamknąć program?")
if odpowiedz:
    print("wcisnieto TAK")
elif odpowiedz is False:
    print("Wcisnieto NIE")
else:
    print("wcisnieto Anuluj")