from sqlite3 import *
def provjera():
    import os
    datoteke = os.listdir(".")
    studenti = {}

    for nazivdatoteke in datoteke:
        if ".txt" in nazivdatoteke:
            datoteka = open(nazivdatoteke, "r")
            for linija in datoteka:
                student = linija.replace("\n", "")
                if student in studenti.keys():
                    studenti[student] += 1
                else:
                    studenti[student] = 1
            datoteka.close()
    return studenti


def provjera_baza():
    konekcija = connect ("skola.db")
    kursor = konekcija.cursor()
    studenti = {}
    for student in kursor.execute("SELECT ime, prezime FROM evidencija"):
        student_str = student[0] + " " + student[1]
        if student_str in studenti.keys():
            studenti[student_str] += 1
        else:
            studenti[student_str] = 1
    '''
    rezultat = kursor.execute("SELECT ime, prezime, COUNT(*) FROM evidencija GROUP BY ime, prezime")
    for student in rezultat:
        studenti[student[0] + " " + student[1]] = studenti[2] 
    '''
    return studenti
