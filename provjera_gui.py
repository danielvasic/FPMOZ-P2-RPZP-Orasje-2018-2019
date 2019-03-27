from tkinter import *
from funkcije.provjera import provjera

studenti = provjera()

master = Tk()
master.title ("Pregled bodova")

Label(master, text="Ime i prezime").grid(row=0, column=0)
Label(master, text="Bodovi").grid(row=0, column=1)

for i, (ime_prezime, bodovi) in enumerate(studenti.items(), 1):
    Label(master, text=ime_prezime).grid(row=i, column=0)
    Label(master, text=bodovi).grid(row=i, column=1)
mainloop()