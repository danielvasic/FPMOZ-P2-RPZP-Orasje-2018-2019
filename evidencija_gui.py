from tkinter import *
from datetime import date
from funkcije.evidencija import dodaj_studenta
from sqlite3 import *

def dodaj_studenta():
    ime = polje1.get()
    prezime = polje2.get()
    # datoteka = open(str(date.today())+"_P2_RPZP.txt", "a")
    # datoteka.write(ime + " " + prezime + "\n")
    # datoteka.close()

    konekcija = connect("skola.db")
    kursor = konekcija.cursor()
    sql = "INSERT INTO evidencija (ID, IME, PREZIME, DATUM) VALUES "
    sql += "(null, '"+ime+"', '"+prezime+"', '"+str(date.today())+"');"
    kursor.execute(sql)
    konekcija.commit()
    konekcija.close()
    polje1.delete(0, END)
    polje2.delete(0, END)

master = Tk()
master.title("Evidencija studenata")
Label(master, text="Ime").grid(row=0)
Label(master, text="Prezime").grid(row=1)
polje1 = Entry(master)
polje2 = Entry(master)
polje1.grid(row=0, column=1)
polje2.grid(row=1, column=1)
Button(master, text="Evidentiraj", command=dodaj_studenta).grid(row=2)
mainloop()