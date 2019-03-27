from datetime import date

datoteka = open(str(date.today())+"_P2_RPZP.txt", "a")
unos = ""
print("Unesite 'izlaz' za izlaz iz programa")

while unos.lower() != "izlaz":
    unos = input("Unesite ime i prezime studenta: ")
    if unos.lower() != "izlaz":
        datoteka.write(unos + '\n')
datoteka.close()
