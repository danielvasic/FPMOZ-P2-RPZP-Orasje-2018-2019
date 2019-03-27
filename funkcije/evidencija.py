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