#Testirajte modul na primjeru proizvoljno odabrane funkcije i raspona integracije.
# Neka korisnik u svom kodu importa modul calculus i za integraciju koristi gotove metode iz tog modula.
#Nacrtajte na istom grafu analitičko riješenje i numerička riješenja za različiti broj koraka i obe metode numeričke integracije.

import calculus
from calculus import pravokutna
from calculus import trapezna
import numpy as np
import matplotlib. pyplot as plt

def funkcija(x):
    return x**2 + 4
 
#print(pravokutna(funkcija, -4, 6, 100))
#print(trapezna(funkcija, -4, 6, 10))

donjaGr=-4
gornjaGr=6

def analiticko(donjaGr, gornjaGr):
    return ((gornjaGr**3)/3 + 4*gornjaGr) - ((donjaGr**3)/3 + 4*donjaGr)

#plot za analiticko rjesenje
xA=np.linspace(10, 1000)
y=np.full_like(xA, analiticko(donjaGr, gornjaGr))
plt.plot(xA, y, color= "red", label="Analitičko rješenje")

particije=np.linspace(10, 1000, 400)

donje_sume=[]
gornje_sume=[]
trapez_sume=[]
for particija in particije:
    particija=int(particija)
    donja_suma, gornja_suma = pravokutna (funkcija, donjaGr, gornjaGr, particija)
    donje_sume.append(donja_suma)
    gornje_sume.append(gornja_suma)
    trapez=trapezna(funkcija, donjaGr, gornjaGr, particija)
    trapez_sume.append(trapez)
    
plt.plot(particije, donje_sume, color= "hotpink", label="Pravokutna suma (donja)")
plt.plot(particije, gornje_sume, color="green", label="Pravokutna suma (gornja)")
plt.plot(particije, trapez_sume, color="blue", label="Trapezna suma")

plt.title("Usporedba analiticke integracije i numerickih aproksimacija")
plt.legend()
plt.grid()
plt.xlabel("broj particija")
plt.ylabel("vrijednosti integrala")
plt.show()