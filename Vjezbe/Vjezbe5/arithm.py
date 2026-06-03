#(b) Napišite program pod (a) koristeći gotove module.
import statistics as stats
import math

n = 10
tocke = [1, 2, 4, 6, 10, 16, 3, 5, 11, 15]

#aritmetička sredina pomoću gotovog modula
srednja_vrijednost = stats.mean(tocke)

#standardna devijacija po zadanoj formuli (koristimo mean iz modula)
sigma=stats.stdev(tocke)

# Ispis rezultata
print(f"Aritmetička sredina s modulima: {srednja_vrijednost}")
print(f"Standardna devijacija s modulima: {sigma}")
