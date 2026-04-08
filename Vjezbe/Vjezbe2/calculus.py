#Napišite modul "calculus.py" koji će sadržavati dvije metode:
#• Prva metoda kao ulazne parametre prima funkciju i točku, a kao rezultat vraća vrijednost derivacije
#funkcije u toj točki.
#• Druga prima kao ulazne parametre funkciju i gornju i donju granicu raspona derivacije. Funkcija korisniku vraća listu točaka 
# u kojima će biti izvršena numerička derivacija na zadanom rasponu i iznose derivacije funkcije u tim istim točkama.
#Testirajte modul na primjerima kubne i trigonometrijske funkcije. Neka korisnik u svom kodu importa
#modul calculus i za derivaciju koristi gotove metode iz tog modula.
#Nacrtajte na istom grafu analitičko rješenje i numerička rješenja za različite korake numeričke derivacije.
#To ćete postići tako da u razvijenim metodama iz modula calculus dodate opciju da metoda 
# kao jedan od ulaznih parametara prima i veličinu koraka derivacije ϵ i metodu kojom derivira.
# Neka "three-step" metoda bude zadana ako korisnik ništa ne odabere, a "two-step" metoda bude druga ponuđena opcija.


import numpy as np
import math

def derivacija_tocka(f, x, epsilon, metoda="three_step"):
    if metoda == "three_step":
        derTocka= (f(x+ epsilon) - f(x - epsilon))/(2*epsilon)
    elif metoda == "two_step":
        derTocka = (f(x + epsilon) - f(x))/epsilon
    else:
        raise ValueError ("Moguće metode su two step i three step")
    
    return derTocka

def derivacija_interval (f, donjaG, gornjaG, epsilon, metoda="three_step"):
    derInterval=[]
    tocke=np.linspace(donjaG, gornjaG, 100)
    for x in tocke:
        derInterval.append(derivacija_tocka(f, x, epsilon, metoda))
    
    return tocke, derInterval

#Prva metoda kao ulazne parametre prima funkciju, granice integracije i broj podjela za numeričku
#integraciju, a vraća gornju i donju među koristeći pravokutnu aproksimaciju.
def meda(f, donjaGr, gornjaGr, N):
    if donjaGr>gornjaGr:
        donjaGr, gornjaGr= gornjaGr, donjaGr
    elif donjaGr==gornjaGr:
        return 0, 0
    else:
        gornja=0
        donja=0
        x=np.linspace(a,b, N+1)
        dx=(gornjaGr-donjaGr)/N
        for i in range(N):
            donja+=f(x)*dx 
        print(donja)
        for i in range(1, n+1):
            gornja+=a

def funkcija(x):
    return x**2
#print(derivacija_tocka(funkcija, 4, 0.0001))
#print(derivacija_interval(funkcija, 6, 8, 0.0001))