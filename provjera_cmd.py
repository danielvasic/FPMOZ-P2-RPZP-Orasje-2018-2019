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

print(studenti)
