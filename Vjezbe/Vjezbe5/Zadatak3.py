#(a) Napišite program arithm.py koji računa aritmetičku sredinu i
# standardnu devijaciju za 10 točaka. Formula za aritmetičku sredinu je dana u 1,
#a za standardnu devijaciju u 2.
#(b) Napišite program pod (a) koristeći gotove module.

n = 10
tocke = [1, 2, 4, 6, 10, 16, 3, 5, 11, 15] #lista tocaka

#Izračun aritmetičke sredine
# suma svih elemenata
srednja_vrijednost =sum(tocke) / n

# Izračun standardne devijacije po zadanoj formuli
sum=0
for tocka in tocke:
    izraz= (tocka - srednja_vrijednost)**2
    sum+=izraz
sigma=(sum/(n*(n-1)))**(1/2)

#Ispis rezultata
print(f"Aritmetička sredina: {srednja_vrijednost}")
print(f"Standardna devijacija: {sigma}")