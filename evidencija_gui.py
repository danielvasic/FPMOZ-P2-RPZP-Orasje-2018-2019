from tkinter import *
from datetime import date
from funkcije.evidencija import dodaj_studenta

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