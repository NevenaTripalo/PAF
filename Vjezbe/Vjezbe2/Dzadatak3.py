#Testirajte modul na primjerima kubne i trigonometrijske funkcije. Neka korisnik u svom kodu importa
#modul calculus i za derivaciju koristi gotove metode iz tog modula.
# Nacrtajte na istom grafu analitičko rješenje i numerička rješenja za različite korake numeričke derivacije.
# To ćete postići tako da u razvijenim
#metodama iz modula calculus dodate opciju da metoda kao jedan od ulaznih parametara prima i ϵ i metodu kojom derivira.

import numpy as np
import matplotlib.pyplot as plt
from calculus import derivacija_tocka as dt 
from calculus import derivacija_interval as di 

#funkcije kojim cemo testiarati
def kubna(x):
    return x**3
def trig(x):
    return np.sin(x)

#analiticka rjesenja zadanih funkcija
def analiticko_kubna(x):
    return 3*x**2
def analiticko_sinus(x):
    return np.cos(x)

donjaGS=-6   #granice za sinusnu
gornjaGS=6

donjaGK=-3
gornjaGK=3

epsiloni=[0.5, 0.1, 0.0001]

plt.subplot(1,2,1)                      #na prvom grafu sinus analiticko i numericka, na drugom kubna i numericka
xs = np.linspace(donjaGS, gornjaGS, 400)        #x raspon za sinusnu funkciju
plt.plot(xs, analiticko_sinus(xs), linewidth=1, color="hotpink", label="Analitička derivacija")
for epsilon in epsiloni:
    tockeS, derivacijeS=di(trig, donjaGS, gornjaGS, epsilon)        #derivacije i tocke za sinusnu funkciju
    plt.scatter(tockeS, derivacijeS, s=8, label=f"ε={epsilon}")
plt.title("sin(x)")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.grid()
plt.legend()


plt.subplot(1, 2, 2)
xk = np.linspace(donjaGK, gornjaGK, 400)        #x raspon za kubnu funkciju
plt.plot(xk, analiticko_kubna(xk), linewidth=1, color= "hotpink", label="Analitička derivacija")
for epsilon in epsiloni:
    tockeK, derivacijeK=di(kubna, donjaGK, gornjaGK, epsilon)       #derivacije i tocke za kubnu funkciju
    plt.scatter(tockeK, derivacijeK, s=8, label=f"ε={epsilon}")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.title("x^3")
plt.legend()
plt.grid()

plt.suptitle("Analiticka i numericke derivacije funkcija")
plt.tight_layout()
plt.show()
