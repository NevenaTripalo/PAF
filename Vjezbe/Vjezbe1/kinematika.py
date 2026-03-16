#Zadatak 2
#Napišite svoj modul "kinematika.py" koji će sadržavati funckiju jednoliko_gibanje(). Neka funkcije kao
#ulazne parametre primaju sve podatke neophodne za izračun (iznos sile, masa, ...) i neka crta iste grafove
#kao i u prošlom zadatku. Napravite novi program u kojem ćete uključiti razvijeni modul i pozvati funkciju.
import matplotlib.pyplot as plt
import numpy as np
def jednoliko_gibanje(sila, masa, t, v0, x0):
    
    if masa<=0:
        raise ValueError("Masa mora biti veća od 0.")
    if t<=0:
        raise ValueError("Morate dati neki vremenski interval veći od nule. ")
    
    # a -t graf
    #a=F/M kod jednolikog gibanja konstantna
    akceleracija=sila/masa
    plt.subplot(1, 3, 1)
    x=np.linspace(0,t, 10)
    y=np.full_like(x,akceleracija)
    plt.grid(True)
    plt.margins(x=0)
    plt.title("Ovisnost akceleracije u vremenu", fontsize=10)
    plt.xlabel("vrijeme [s]")
    plt.ylabel("akceleracija [m/s^2]")
    plt.plot(x,y, color="hotpink")

    # v- t graf
    #v(t)=v0 + at
    #brzina=v0 + akceleracija*t
    plt.subplot(1, 3, 2)
    x=np.linspace(0, t, 10)
    brzina=v0 + akceleracija*x
    y=brzina
    plt.grid(True)
    plt.margins(x=0)
    plt.title("Ovisnost brzine u vremenu", fontsize=10)
    plt.xlabel("vrijeme [s]")
    plt.ylabel("brzina [m/s]")
    plt.plot(x,y, color="red")

    # x -t graf
    #x=x0 + v0t + at^2/2
    plt.subplot(1, 3, 3)
    x=np.linspace(0, t, 50)
    put=x0 + v0*t + (akceleracija*x**2)/2
    y=put
    plt.grid(True)
    plt.margins(x=0)
    plt.title("Ovisnost puta u vremenu", fontsize=10)
    plt.xlabel("vrijeme [s]")
    plt.ylabel("put [m]")
    plt.plot(x,y, color="blue")

    plt.tight_layout()
    plt.show()